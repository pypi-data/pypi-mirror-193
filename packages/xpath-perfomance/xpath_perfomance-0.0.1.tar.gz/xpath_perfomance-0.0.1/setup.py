from setuptools import setup

with open("README.rst", "r", encoding="utf-8") as fh:
    readme = fh.read()

setup(name='xpath_perfomance',
      version='0.0.1',
      license='Code Distribution License',
      author='Parceiro do Contador',
      author_email='parceiro@parceirodocontador.com.br',
      keywords='selenium xpath',
      description=u'Wrapper for Selenium to make it more easy and efficient to use',
      long_description=readme,
      long_description_content_type="text/x-rst",
      packages=['xperfomance'],
      install_requires=['selenium', 'webdriver-manager', 'pyperclip'],
      include_package_data=True)
