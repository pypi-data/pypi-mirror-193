from typing import Optional

class InstallProgressHandler(object):
    def __init__(self, module_name: str="", module_version: Optional[str]=None):
        self.module_name = module_name
        self.module_version = module_version
        self.display_name = None
        self.cur_stage = None
        self.install_state = None
        if module_name:
            self._make_display_name()

    def set_module(self, module_name: str="", module_version: Optional[str]=None):
        self.module_name = module_name
        self.module_version = module_version
        if module_name:
            self._make_display_name()

    def _make_display_name(self):
        ver_str = self.module_version if self.module_version is not None else ""
        self.display_name = ":".join([self.module_name, ver_str])

    def stage_start(self, __stage__):
        pass

    def set_module_version(self, module_version):
        self.module_version = module_version
        self._make_display_name()

    def _stage_msg(self, stage):
        from ..util.util import get_current_time_str

        if stage is None or stage == "":
            return ""
        elif stage == "start":
            return (
                f"[{get_current_time_str()}] Starting to install {self.display_name}..."
            )
        elif stage == "download_code":
            return f"[{get_current_time_str()}] Downloading code archive of {self.display_name}..."
        elif stage == "extract_code":
            return f"[{get_current_time_str()}] Extracting code archive of {self.display_name}..."
        elif stage == "verify_code":
            return f"[{get_current_time_str()}] Verifying code integrity of {self.display_name}..."
        elif stage == "download_data":
            return (
                f"[{get_current_time_str()}] Downloading data of {self.display_name}..."
            )
        elif stage == "extract_data":
            return (
                f"[{get_current_time_str()}] Extracting data of {self.display_name}..."
            )
        elif stage == "verify_data":
            return f"[{get_current_time_str()}] Verifying data integrity of {self.display_name}..."
        elif stage == "finish":
            return f"[{get_current_time_str()}] finished installation of {self.display_name}"
        elif stage == "killed":
            return f"[{get_current_time_str()}] Aborted installation of {self.display_name}"
        elif stage == "Unqueued":
            return f"Unqueued {self.display_name} from installation"
        else:
            return f"[{get_current_time_str()}] {stage}"


def get_readme(module_name):
    from os.path import exists
    from ..store import remote_module_latest_version
    from ..store.db import get_latest_module_code_version
    from .local import module_exists_local
    from .cache import get_module_cache
    from .local import get_local_module_info
    from ..util.util import compare_version

    exists_local = module_exists_local(module_name)
    remote_ver = get_latest_module_code_version(module_name)
    if remote_ver:
        remote_readme = get_module_cache().get_remote_readme(
            module_name, version=remote_ver
        )
    else:
        remote_readme = ""
    if exists_local:
        local_info = get_local_module_info(module_name)
        if local_info and exists(local_info.readme_path):
            local_readme = open(local_info.readme_path, encoding="utf-8").read()
        else:
            local_readme = ""
        if local_info and remote_ver:
            remote_version = remote_module_latest_version(module_name)
            local_version = local_info.version
            if compare_version(remote_version, local_version) > 0:
                return remote_readme
            else:
                return local_readme
        else:
            return local_readme
    else:
        local_readme = ""
        if remote_ver:
            return remote_readme
        else:
            return local_readme


def install_pypi_dependency(args={}):
    from subprocess import run
    from ..util.util import quiet_print

    pypi_dependency = args.get("pypi_dependency")
    if not pypi_dependency:
        pypi_dependency = args.get("pypi_dependencies")
    if not pypi_dependency:
        pypi_dependency = args.get("requires_pypi")
    idx = 0
    if pypi_dependency:
        quiet_print(
            f"Following PyPI dependencies should be met before installing {args.get('module_name')}.",
            args=args,
        )
        for dep in pypi_dependency:
            quiet_print(f"- {dep}", args=args)
        quiet_print(f"Installing required PyPI packages...", args=args)
        idx = 0
        while idx < len(pypi_dependency):
            dep = pypi_dependency[idx]
            r = run(["pip", "install", dep])
            if r.returncode == 0:
                pypi_dependency.remove(dep)
            else:
                idx += 1
        if len(pypi_dependency) > 0:
            quiet_print(
                f"Following PyPI dependencies could not be installed.",
                args=args,
            )
            for dep in pypi_dependency:
                quiet_print(f"- {dep}", args=args)
    if pypi_dependency:
        quiet_print(
            f"Skipping installation of {args.get('module_name')} due to unmet requirement for PyPI packages",
            args=args,
        )
        return False
    else:
        return True


def list_local():
    from ..system import get_modules_dir
    from .cache import get_module_cache

    modules_dir = get_modules_dir()
    module_cache = get_module_cache()
    if module_cache._modules_dir != modules_dir:
        module_cache._modules_dir = modules_dir
        module_cache.update_local()
    return sorted(list(get_module_cache().get_local().keys()))


def list_remote(module_type=None):
    from ..store.db import module_list

    return module_list(module_type=module_type)


def get_updatable(modules=[], requested_modules=[], strategy="consensus"):
    from packaging.version import Version
    from pkg_resources import Requirement
    from collections import defaultdict
    from types import SimpleNamespace
    from .local import get_local_module_info
    from .remote import get_remote_module_info
    from ..store.db import remote_module_data_version

    if strategy not in ("consensus", "force", "skip"):
        raise ValueError('Unknown strategy "{}"'.format(strategy))
    if not modules:
        modules = list_local()
    else:
        modules = requested_modules
    reqs_by_dep = defaultdict(dict)
    all_versions = {}
    for mname in list_local():
        local_info = get_local_module_info(mname, fresh=True)
        remote_info = get_remote_module_info(mname)
        if remote_info:
            all_versions[mname] = sorted(remote_info.versions, key=Version)
        if local_info:
            req_strings = local_info.conf.get("requires", [])
            reqs = [Requirement.parse(s) for s in req_strings]
            for req in reqs:
                dep = req.unsafe_name
                reqs_by_dep[dep][mname] = req
    update_vers = {}
    resolution_applied = {}
    resolution_failed = {}
    for mname in modules:
        if mname not in list_local():
            continue
        local_info = get_local_module_info(mname)
        remote_info = get_remote_module_info(mname)
        reqs = reqs_by_dep[mname]
        versions = all_versions.get(mname, [])
        if not versions:
            continue
        selected_version = versions[-1]
        if (
            selected_version
            and local_info
            and local_info.version
            and Version(selected_version) <= Version(local_info.version)
        ):
            continue
        if reqs:
            resolution_applied[mname] = reqs
            if strategy == "force":
                pass
            elif strategy == "skip":
                selected_version = None
            elif strategy == "consensus":
                passing_versions = []
                for version in versions:
                    version_passes = True
                    for _, requirement in reqs.items():
                        version_passes = version in requirement
                        if not version_passes:
                            break
                    if version_passes:
                        passing_versions.append(version)
                selected_version = passing_versions[-1] if passing_versions else None
        if (
            selected_version
            and remote_info
            and local_info
            and local_info.version
            and Version(selected_version) > Version(local_info.version)
        ):
            update_data_version = remote_module_data_version(mname, selected_version)
            installed_data_version = remote_module_data_version(
                mname, local_info.version
            )
            if (
                update_data_version is not None
                and update_data_version != installed_data_version
            ):
                update_size = remote_info.size
            else:
                update_size = remote_info.code_size
            update_vers[mname] = SimpleNamespace(
                version=selected_version, size=update_size
            )
        else:
            resolution_failed[mname] = reqs
    return update_vers, resolution_applied, resolution_failed


def make_install_temp_dir(args={}):
    from ..system import get_modules_dir
    from ..consts import install_tempdir_name
    from shutil import rmtree
    from pathlib import Path

    modules_dir: Optional[str] = args.get("modules_dir")
    if not modules_dir:
        modules_dir = get_modules_dir()
    if not modules_dir:
        raise
    module_name: Optional[str] = args.get("module_name")
    if not module_name:
        raise
    temp_dir = (
        Path(modules_dir) / install_tempdir_name / module_name
    )
    if args.get("clean"):
        rmtree(str(temp_dir), ignore_errors=True)
    temp_dir.mkdir(parents=True, exist_ok=True)
    args["temp_dir"] = str(temp_dir)
    return temp_dir


def set_stage_handler(args={}):
    if args:
        pass
    if not args.get("stage_handler"):
        args["stage_handler"] = InstallProgressHandler(
            args.get("module_name"), args.get("version")
        )
        args["stage_handler"].set_module_version(args.get("version"))
    if hasattr(args.get("stage_handler"), "install_state") == True:
        args["install_state"] = args.get("stage_handler").install_state  # type: ignore
    else:
        args["install_state"] = None


def get_pypi_dependency_from_conf(conf={}):
    if not conf:
        return []
    pypi_dependency = []
    for key in ["pypi_dependency", "pypi_dependencies", "requires_pypi"]:
        vals = conf.get(key) or []
        for v in vals:
            if v not in pypi_dependency:
                pypi_dependency.append(v)
    return pypi_dependency


def check_install_kill(args={}, install_state=None, module_name=None):
    from ..exceptions import KillInstallException

    if not install_state:
        install_state = args.get("install_state")
    if not module_name:
        module_name = args.get("module_name")
        if not module_name:
            module_name = install_state.get("module_name")
    if install_state and module_name and install_state["module_name"] == module_name and install_state["kill_signal"] == True:
        raise KillInstallException


def get_download_zipfile_path(args={}, kind=None):
    from pathlib import Path
    if "module_name" not in args or "version" not in args or "temp_dir" not in args or kind is None:
        return None
    zipfile_fname = (
        args.get("module_name") + "__" + args.get(f"version") + f"__{kind}.zip"
    )
    zipfile_path = str(Path(args.get("temp_dir")) / zipfile_fname)
    return zipfile_path

def download_code_or_data(kind=None, args={}, install_state=None):
    from pathlib import Path
    from os.path import getsize
    from os import remove
    from json import loads
    from ..util.download import download
    from ..store.consts import MODULE_PACK_SPLIT_FILE_SIZE
    from ..util.util import quiet_print

    check_install_kill(args=args)
    if not kind or kind not in ["code", "data"]:
        return
    if args.get("stage_handler"):
        args.get("stage_handler").stage_start(f"download_{kind}")
    zipfile_path = get_download_zipfile_path(args=args, kind=kind)
    if not zipfile_path:
        return False
    urls = args.get(f"{kind}_url")
    if urls[0] == "[":  # a list of URLs
        urls = loads(urls)
    urls_ty = type(urls)
    if urls_ty == str:
        download(args.get(f"{kind}_url"), zipfile_path, install_state=install_state, check_install_kill=check_install_kill)
    elif urls_ty == list:
        download_from = 0
        if Path(zipfile_path).exists():
            zs = getsize(zipfile_path)
            if zs % MODULE_PACK_SPLIT_FILE_SIZE == 0:
                # partial download completed
                download_from = int(getsize(zipfile_path) / MODULE_PACK_SPLIT_FILE_SIZE)
            else:
                remove(zipfile_path)
        with open(zipfile_path, "ab") as wf:
            urls_len = len(urls)
            for i in range(urls_len):
                if i < download_from:
                    continue
                part_path = f"{zipfile_path}{i:03d}"
                if (
                    Path(part_path).exists()
                    and getsize(part_path) == MODULE_PACK_SPLIT_FILE_SIZE
                ):
                    continue
                download(urls[i], part_path, install_state=install_state, check_install_kill=check_install_kill)
                if i < urls_len - 1:
                    if getsize(part_path) != MODULE_PACK_SPLIT_FILE_SIZE:
                        quiet_print(
                            f"corrupt download {part_path} at {urls[i]}", args=args
                        )
                        remove(part_path)
                        return False
                with open(part_path, "rb") as f:
                    wf.write(f.read())
                remove(part_path)
    args[f"{kind}_zipfile_path"] = zipfile_path
    return True


def extract_code_or_data(kind=None, args={}):
    import zipfile
    from os import remove

    check_install_kill(args=args)
    if not kind or kind not in ["code", "data"]:
        return
    if args.get("stage_handler"):
        args.get("stage_handler").stage_start(f"extract_{kind}")
    zf = zipfile.ZipFile(args.get(f"{kind}_zipfile_path"))
    zf.extractall(args.get("temp_dir"))
    zf.close()
    remove(args.get(f"{kind}_zipfile_path"))


def cleanup_install(args={}):
    from pathlib import Path
    from shutil import rmtree
    from shutil import move
    from os import listdir
    from pathlib import Path
    from .local import remove_code_part_of_module

    module_dir = args.get("module_dir")
    temp_dir = args.get("temp_dir")
    # Unsuccessful installation
    if not args.get("installation_finished"):
        return
    # New installation
    if not Path(module_dir).exists():
        move(temp_dir, module_dir)
        return
    # Update
    if args.get("data_installed"):
        rmtree(module_dir)
        move(temp_dir, module_dir)
    elif args.get("code_installed"):
        remove_code_part_of_module(args.get("module_name"))
        for item in listdir(temp_dir):
            old_path = Path(temp_dir) / item
            new_path = Path(module_dir) / item
            if item != "data":
                move(str(old_path), new_path)
        rmtree(temp_dir)


def write_install_marks(args={}):
    from os.path import join

    module_dir = args.get("module_dir")
    wf = open(join(module_dir, "startofinstall"), "w")
    wf.close()
    wf = open(join(module_dir, "endofinstall"), "w")
    wf.close()


def install_module_from_url(module_name: str, url: str, stage_handler: Optional[InstallProgressHandler]=None, args={}):
    from pathlib import Path
    from shutil import move
    from shutil import rmtree
    from zipfile import ZipFile
    from urllib.parse import urlparse
    from os import remove
    from ..system import get_modules_dir
    from ..util.download import download
    from ..util.util import load_yml_conf
    from ..util.util import quiet_print
    from .remote import get_install_deps
    from ..exceptions import ArgumentError

    args["module_name"] = module_name
    temp_dir = make_install_temp_dir(args=args)
    if temp_dir.parent.name == module_name:
        download(url, temp_dir.parent)
    else:
        fname = Path(urlparse(url).path).name
        if Path(fname).suffix != ".zip":
            raise ArgumentError(msg=f"--url should point to a zip file of a module.")
        fpath = temp_dir / fname
        download(url, fpath)
        with ZipFile(fpath) as f:
            f.extractall(path=temp_dir)
        remove(fpath)
    yml_conf_path = temp_dir / (module_name + ".yml")
    if not yml_conf_path.exists():
        quiet_print(
            f"{url} is not a valid OakVar module. {module_name}.yml should exist.",
            args=args,
        )
        return False
    conf = load_yml_conf(yml_conf_path)
    args["conf"] = conf
    if not args.get("skip_dependencies"):
        deps, deps_pypi = get_install_deps(conf_path=str(yml_conf_path))
        args["pypi_dependency"] = deps_pypi
        if not install_pypi_dependency(args=args):
            quiet_print(f"failed in installing pypi package dependence", args=args)
            return False
        for deps_mn, deps_ver in deps.items():
            install_module(
                deps_mn,
                version=deps_ver,
                stage_handler=stage_handler,
                force_data=args["force_data"],
                skip_data=args["skip_data"],
                quiet=args["quiet"],
                args=args,
            )
    ty = conf.get("type") or ""
    if not ty:
        quiet_print(
            f"{url} is not a valid OakVar module. {module_name}.yml does not have 'type' field.",
            args=args,
        )
        return False
    modules_dir = Path(get_modules_dir())
    module_type_dir = modules_dir / (ty + "s")
    if not module_type_dir.exists():
        module_type_dir.mkdir()
    module_dir = module_type_dir / module_name
    if module_dir.exists():
        if args.get("force") or args.get("overwrite"):
            rmtree(str(module_dir))
        else:
            quiet_print(f"{module_dir} already exists.", args=args)
            return False
    move(str(temp_dir), str(module_type_dir))
    return True


def install_module_from_zip_path(path: str, args: dict = {}):
    from pathlib import Path
    from ..util.util import load_yml_conf
    from ..util.util import quiet_print
    from ..util.util import get_random_string
    from ..util.util import load_yml_conf
    from ..exceptions import ExpectedException
    from .local import get_new_module_dir
    from .remote import get_install_deps
    from shutil import copytree
    from shutil import rmtree
    from zipfile import ZipFile

    f = ZipFile(path)
    temp_dir = "oakvar_temp_dir__" + get_random_string(k=16)
    try:
        while Path(temp_dir).exists():
            temp_dir = "oakvar_temp_dir__" + get_random_string(k=16)
        f.extractall(path=temp_dir)
        children = [v for v in Path(temp_dir).iterdir()]
        if len(children) > 1:
            raise ExpectedException(msg=f"Only 1 module folder should exist in {path}.")
        temp_module_path = children[0]
        if not temp_module_path.is_dir():
            raise ExpectedException(msg=f"1 module folder should exist in {path}.")
        yml_paths = [v for v in temp_module_path.glob("*.yml")]
        if len(yml_paths) > 1:
            raise ExpectedException(
                msg=f"Only 1 module config file should exist in {str(temp_module_path)}."
            )
        yml_path = yml_paths[0]
        module_name = yml_path.stem
        args["module_name"] = module_name
        f = open(str(yml_path))
        conf = load_yml_conf(str(yml_path))
        module_type = conf.get("type")
        if not module_type:
            raise ExpectedException(
                msg=f"Module type should be defined in {module_name}.yml."
            )
        module_dir = get_new_module_dir(module_name, module_type)
        if not module_dir:
            raise ExpectedException(msg=f"{module_dir} could not be created.")
        # dependencies
        deps, deps_pypi = get_install_deps(conf_path=str(yml_path))
        args["pypi_dependency"] = deps_pypi
        if not install_pypi_dependency(args=args):
            raise ExpectedException("failed in installing pypi package dependence")
        for deps_mn, deps_ver in deps.items():
            install_module(
                deps_mn,
                version=deps_ver,
                force_data=args["force_data"],
                skip_data=args["skip_data"],
                quiet=args["quiet"],
                args=args,
            )
        # move module
        copytree(str(temp_module_path), module_dir, dirs_exist_ok=True)
        quiet_print(f"{module_name} installed at {module_dir}", args=args)
        rmtree(temp_dir)
        return True
    except Exception as e:
        rmtree(temp_dir)
        raise e


def get_module_install_version(module_name, version=None, fresh=False, args={}) -> str:
    from packaging.version import Version
    from ..module.local import get_local_module_info
    from ..module.remote import get_remote_module_info
    from ..exceptions import ModuleNotExist
    from ..exceptions import ModuleVersionError
    from ..exceptions import ModuleToSkipInstallation

    local_info = get_local_module_info(module_name, fresh=fresh)
    remote_info = get_remote_module_info(module_name)
    if not remote_info:
        raise ModuleNotExist(module_name)
    if not version and remote_info:
        version = remote_info.latest_code_version
    if not version:
        raise ModuleNotExist(module_name)
    if not remote_info:
        raise ModuleVersionError(module_name, version)
    if (
        not args.get("overwrite")
        and local_info
        and Version(local_info.code_version or "") == Version(version)
    ):
        raise ModuleToSkipInstallation(
            module_name,
            msg=f"{module_name}=={version} already exists.",
        )
    if (
        (not args.get("overwrite"))
        and local_info
        and local_info.code_version
        and Version(local_info.code_version or "") >= Version(version)
    ):
        raise ModuleToSkipInstallation(
            module_name,
            msg=f"{module_name}: Local version ({local_info.code_version}) is higher than the latest store version ({version}). Use --overwrite to overwrite.",
        )
    else:
        return version


def install_module(
    module_name,
    version=None,
    force_data=False,
    skip_data=False,
    stage_handler: Optional[InstallProgressHandler]=None,
    quiet=True,
    conf_path=None,
    fresh=False,
    args={},
):
    from os.path import join
    from ..exceptions import KillInstallException
    from ..exceptions import ModuleInstallationError
    from ..store import get_module_urls
    from ..store.db import remote_module_data_version
    from ..store.db import summary_col_value
    from .cache import get_module_cache
    from .remote import get_conf
    from .local import get_module_data_version as local_module_data_version
    from ..util.util import quiet_print
    from ..system import get_modules_dir

    if stage_handler:
        stage_handler.set_module(module_name=module_name, module_version=version)
    version = get_module_install_version(module_name, version=version, fresh=fresh, args=args)
    args["quiet"] = quiet
    args["module_name"] = module_name
    args["version"] = version
    args["stage_handler"] = stage_handler
    quiet_print(f"installing {module_name}...", args=args)
    args["code_version"] = version
    make_install_temp_dir(args=args)
    try:
        args["installation_finished"] = False
        args["code_installed"] = False
        args["data_installed"] = False
        set_stage_handler(args=args)
        args.get("stage_handler").stage_start("start")
        args["conf"] = get_conf(module_name=module_name, conf_path=conf_path) or {}
        args["pypi_dependency"] = get_pypi_dependency_from_conf(conf=args.get("conf"))
        # Checks and installs pip packages.
        if not install_pypi_dependency(args=args):
            quiet_print(f"failed in installing pypi package dependence", args=args)
            raise ModuleInstallationError(module_name)
        args["remote_data_version"] = remote_module_data_version(
            args.get("module_name"), args.get("code_version")
        )
        args["local_data_version"] = local_module_data_version(args.get("module_name"))
        r = get_module_urls(module_name, code_version=version)
        if not r:
            quiet_print(f"failed in getting module URLs", args=args)
            raise ModuleInstallationError(module_name)
        args["code_url"], args["data_url"] = r.get("code_url"), r.get("data_url")
        args["module_type"] = summary_col_value(args.get("module_name"), "type")
        if not args.get("module_type"):
            # Private module. Fallback to remote config.
            args["module_type"] = args.get("conf").get("type")
        if not args.get("module_type"):
            quiet_print(f"module type not found", args=args)
            raise ModuleInstallationError(module_name)
        if not args.get("modules_dir"):
            args["modules_dir"] = get_modules_dir()
        args["module_dir"] = join(
            args.get("modules_dir"),
            args.get("module_type") + "s",
            args.get("module_name"),
        )
        install_state = stage_handler.install_state if stage_handler else None
        if not download_code_or_data(kind="code", args=args, install_state=install_state):
            quiet_print(f"code download failed", args=args)
            raise ModuleInstallationError(module_name)
        extract_code_or_data(kind="code", args=args)
        args["code_installed"] = True
        if (
            not skip_data
            and args.get("remote_data_version")
            and (
                args.get("remote_data_version") != args.get("local_data_version")
                or force_data
            )
        ):
            if not args.get("data_url"):
                quiet_print(f"data_url is empty.", args=args)
                raise ModuleInstallationError(module_name)
            if not download_code_or_data(kind="data", args=args, install_state=install_state):
                quiet_print(f"data download failed", args=args)
                raise ModuleInstallationError(module_name)
            extract_code_or_data(kind="data", args=args)
            args["data_installed"] = True
        args["installation_finished"] = True
        cleanup_install(args=args)
        write_install_marks(args=args)
        get_module_cache().update_local()
        args.get("stage_handler").stage_start("finish")
        return True
    # except (Exception, KeyboardInterrupt, SystemExit) as e:
    except Exception as e:
        if isinstance(e, ModuleInstallationError):
            import traceback
            traceback.print_exc()
            cleanup_install(args=args)
        elif isinstance(e, KillInstallException) or isinstance(e, ModuleInstallationError):
            if stage_handler:
                stage_handler.stage_start("killed")
            cleanup_install(args=args)
        elif isinstance(e, KeyboardInterrupt):
            # signal.signal(signal.SIGINT, original_sigint)
            raise e
        elif isinstance(e, SystemExit):
            return False
        else:
            cleanup_install(args=args)
            # signal.signal(signal.SIGINT, original_sigint)
            raise e
    # finally:
    #    signal.signal(signal.SIGINT, original_sigint)


def uninstall_module(module_name, args={}):
    import shutil
    from .local import get_local_module_info
    from .cache import get_module_cache
    from ..util.util import quiet_print

    if not module_name in list_local():
        quiet_print(f"{module_name} does not exist.", args=args)
        return False
    local_info = get_local_module_info(module_name)
    if not local_info:
        quiet_print(f"{module_name} does not exist.", args=args)
        return False
    shutil.rmtree(local_info.directory)
    mc = get_module_cache()
    mc.remove_local(module_name)

