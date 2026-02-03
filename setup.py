from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',  # بدون فراغ
    version='0.0.1',
    packages=find_packages(),  # تحطها مرة واحدة بس
    author_email='marwan.yasser644@gmail.com',  # صحح البريد
    install_requires=get_requirements('requirements.txt')  # اسم الملف صح
)
