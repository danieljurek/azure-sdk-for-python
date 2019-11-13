import argparse
from packaging.version import parse

from version_shared import get_packages, set_version_py, set_dev_classifier

DEFAULT_SDK_PATH = "../../sdk/"

def increment_version(old_version):
    parsed_version = parse(old_version)
    release = parsed_version.release

    if parsed_version.is_prerelease:
        prerelease_version = parsed_version.pre[1]
        return f'{release[0]}.{release[1]}.{release[2]}b{prerelease_version + 1}'

    return f'{release[0]}.{release[1] + 1}.0b1'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Increments version for a given package name based on the released version')
    parser.add_argument('--sdk-path', default=DEFAULT_SDK_PATH, help='path to the sdk folder')
    parser.add_argument('--package-name', required=True, help='name of package (accetps both formats: azure-service-package and azure_service_pacage)')

    args = parser.parse_args()

    package_name = args.package_name.replace('_', '-')

    packages = get_packages(args.sdk_path)
    package_map = { pkg[1][0]: pkg for pkg in packages }

    if package_name not in package_map:
        raise ValueError("Package name not found: %s" % package_name)

    target_package = package_map[package_name]

    new_version = increment_version(target_package[1][1])
    print(f'{package_name}: {target_package[1][1]} -> {new_version}')

    set_version_py(target_package[0], new_version)
    set_dev_classifier(target_package[0], new_version)