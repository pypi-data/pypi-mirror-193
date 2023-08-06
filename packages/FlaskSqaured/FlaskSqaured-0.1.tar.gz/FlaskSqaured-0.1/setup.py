
from distutils.core import setup
setup(
  name = 'FlaskSqaured',        
  packages = ['FlaskSqaured'],   
  version = '0.1',      
  license='MIT',        
  description = 'An easier and more simple version of flask.',
  author = 'WhMonkey',                   
  author_email = 'no-reply@no-reply.com',      
  url = 'https://github.com/WhineyMonkey10/easyflask',   
  download_url = 'https://github.com/WhineyMonkey10/FlaskSqaured/archive/refs/tags/v.0.1.3.tar.gz',    
  keywords = ['FLASK', 'WEBSITE', 'EASY'],   
  install_requires=[            
          'flask',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)