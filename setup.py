from distutils.core import setup
setup(
  name='bigQueryExporter',
  packages=['bigQueryExporter'],  # this must be the same as the name above
  version='1.0.1',
  description='Package codes to execute queries on BigQuery and save to local machine',
  author='Icarus So (enhanced by Jason Tsang)',
  author_email='icarus.so@gmail.com',
  url='https://github.com/tsangkinhoi/bigQueryExporter-enhanced',  # use the URL to the github repo
  keywords=['bigquery', 'local', 'export'],  # arbitrary keywords
  classifiers=[],
  install_requires=[
      'google-api-core==0.1.4',
      'google-auth==1.3.0',
      'google-cloud-bigquery==0.29.0',
      'google-cloud-core==0.28.0',
      'google-cloud-storage==1.7.0',
      'googleapis-common-protos==1.5.3',
      'pandas==0.22.0',
  ]
)