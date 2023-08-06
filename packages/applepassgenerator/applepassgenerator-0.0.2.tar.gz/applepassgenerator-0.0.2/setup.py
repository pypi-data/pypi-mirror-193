# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['applepassgenerator']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=37.0.2,<38.0.0']

setup_kwargs = {
    'name': 'applepassgenerator',
    'version': '0.0.2',
    'description': 'Python package to create passes compatible with Apple Wallet.',
    'long_description': '# Apple Pass Generator\n\nPython library to generate passes i.e (.pkpass) files compatible with Apple Wallet (former Passbook).\n\n## Table of Contents\n\n- [💾 Installation](#-installation)\n- [🍎 Apple docs](#-apple-docs)\n- [📝 Configuration](#-configuration)\n- [🚀 Usage](#-usage)\n- [📜 Code Of Conduct](#code-of-conduct)\n\n### 💾 Installation\n\nTo easily install or upgrade to the latest release, use pip.\n\n```\n$ pip install applepassgenerator\n```\n\n### 🍎 Apple docs\n\nFrom now on, some stuff is much better explained on the Apple docs, so when in doubt just check (if you haven\'t done so) the following documents:\n\n- [Wallet Portal](https://developer.apple.com/wallet/)\n- [Wallet Developer Guide](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)\n- [Crypto Signatures](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/PassKit_PG/Creating.html#//apple_ref/doc/uid/TP40012195-CH4-SW55)\n- [PassKit Package Format Reference](https://developer.apple.com/library/ios/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012026)\n\n### 📝 Configuration\n\nTo start using the lib, some Apple files are needed, as well as some action in order to convert them to more friendly formats:\n\n- Get Pass Type ID\n    - Go to the [Apple Developer page ➵ Identifiers ➵ Pass Type IDs](https://developer.apple.com/account/ios/identifiers/passTypeId/passTypeIdList.action).\n    - Next, you need to create a pass type ID. This is similar to the bundle ID for apps. It will uniquely identify a specific kind of pass. It should be of the form of a reverse-domain name style string (i.e., pass.com.example.appname).\n\n- Generate the necessary certificate\n    - After creating the pass type ID, click on Edit and follow the instructions to create a new Certificate.\n    - Once the process is finished, the pass certificate can be downloaded. That\'s not it though, the certificate is downloaded as `.cer` file, which need to be converted to `.p12` in order to work. If you are using a Mac you can import it into Keychain Access and export it as `.p12`from there.\n    - if now you have `certificate.p12` file follow the steps below to convert it to `certifictate.pem`\n\n        ```markdown\n        $ openssl pkcs12 -in certificate.p12 -clcerts -nokeys -out certificate.pem\n        ```\n\n- Generate the key.pem\n\n    ```markdown\n    >$ openssl pkcs12 -in certificate.p12 -nocerts -out private.key\n    ```\n\n    Note: While generating this `private.key` file you will be asked for a PEM pass phrase which will be used as the `CERTIFICATE_PASSWORD` attribute throughout the Package.\n\n- Getting WWDR Certificate\n\n    - If you have made iOS development, you probably have already the Apple Worldwide Developer Relations Intermediate Certificate in your Mac’s keychain.\n    - If not, it can be downloaded from the [Apple Website](https://www.apple.com/certificateauthority/) (on `.cer` format). This one needs to be exported as `.pem`, It can be exported from KeyChain into a `.pem` (e.g. wwdr.pem).\n\n### 🚀 Usage\n\n```python\nfrom applepassgenerator import ApplePassGeneratorClient\nfrom applepassgenerator.models import EventTicket\n\ncard_info = EventTicket()\ncard_info.add_primary_field(\'name\', \'Tony Stark\', \'Name\')\ncard_info.add_secondary_field(\'loc\', \'USA\', \'Country\')\n\nteam_identifier = "1234ABCDEF"\npass_type_identifier = "pass.com.project.example"\norganization_name = "Primedigital Global"\n\napplepassgenerator_client = ApplePassGeneratorClient(team_identifier, pass_type_identifier, organization_name)\napple_pass = applepassgenerator_client.get_pass(card_info)\n\n# Add logo/icon/strip image to file\napple_pass.add_file("logo.png", open("<path>/logo.png", "rb"))\napple_pass.add_file("icon.png", open("<path>/icon.png", "rb"))\n\nCERTIFICATE_PATH = "<path-to-file>/certificate.pem"\nPASSWORD_KEY = "<path-to-file>/password.key"\nWWDR_CERTIFICATE_PATH = "<path-to-file>/wwdr.pem"\nCERTIFICATE_PASSWORD = "<password>"\nOUTPUT_PASS_NAME = "mypass.pkpass"\n\napple_pass.create(CERTIFICATE_PATH, PASSWORD_KEY, WWDR_CERTIFICATE_PATH, CERTIFICATE_PASSWORD, OUTPUT_PASS_NAME)\n```\n\n### Code of Conduct\n\nIn order to foster a kind, inclusive, and harassment-free community, we have a code of conduct, which can be found [here](CODE_OF_CONDUCT.md). We ask you to treat everyone as a smart human programmer that shares an interest in Python and Apple Pass Generator with you.\n',
    'author': 'Primedigital Global',
    'author_email': 'oss@primedigital.tech',
    'maintainer': 'Vikalp Jain',
    'maintainer_email': 'vikalp@primedigital.tech',
    'url': 'https://primedigitalglobal.github.io/applepassgenerator',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
