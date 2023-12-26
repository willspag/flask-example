import pkg_resources

def print_package_version(package_name):
    try:
        version = pkg_resources.get_distribution(package_name).version
        print(f"{package_name}=={version}")
    except pkg_resources.DistributionNotFound:
        print(f"{package_name} is not installed.")

print_package_version("python-dotenv")
print_package_version("Flask")
print_package_version("gunicorn")
print_package_version("flask-wtf")

