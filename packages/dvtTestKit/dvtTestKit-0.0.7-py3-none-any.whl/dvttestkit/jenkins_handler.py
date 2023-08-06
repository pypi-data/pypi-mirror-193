import os
import subprocess


def build_job_jenkins(jenkins_url=os.getenv('jenkins_url'),
                      username=os.getenv('jenkins_username'),
                      api_token=os.getenv('jenkins_api_token'),
                      job_name=os.getenv('jenkins_job_name'),
                      testkit_debug=os.getenv('testkit_debug'),
                      cdrouter_restart=os.getenv('cdrouer_restart'),
                      cdrouter_device=os.getenv('cdrouter_device'),
                      cdrouter_config=os.getenv('cdrouter_config'),
                      cdrouter_package=os.getenv('cdrouter_package'),
                      cdrouter_test=os.getenv('cdrouter_test'),
                      cdrouter_tests=os.getenv('cdrouter_tests'),
                      TicketKey=os.getenv('TicketKey'),
                      tags=os.getenv('tags'),
                      cdrouter_skipUpload=os.getenv('cdrouter_skipUpload'),
                      cdrouter_message=os.getenv('cdrouter_message')):
    """Build a Jenkins job with the specified parameters.

       Args:
           jenkins_url (str): URL of the Jenkins server. Defaults to the JENKINS_URL environment variable.
           username (str): Username for authentication. Defaults to the JENKINS_USERNAME environment variable.
           api_token (str): API token for authentication. Defaults to the JENKINS_API_TOKEN environment variable.
           job_name (str): Name of the Jenkins job to build. Defaults to the JENKINS_JOB_NAME environment variable.
           testkit_debug (str): Whether to enable testkit debug mode. Defaults to the TESTKIT_DEBUG environment variable.
           cdrouter_restart (str): Whether to restart the CDRouter system before running the test. Defaults to the CDROUER_RESTART environment variable.
           cdrouter_device (str): The name of the CDRouter test device. Defaults to the CDROUTER_DEVICE environment variable.
           cdrouter_config (str): The name of the CDRouter config file to use. Defaults to the CDROUTER_CONFIG environment variable.
           cdrouter_package (str): The name of the CDRouter test package to run. Defaults to the CDROUTER_PACKAGE environment variable.
           cdrouter_test (str): The name of the CDRouter test case to run. Defaults to the CDROUTER_TEST environment variable.
           cdrouter_tests (str): The name(s) of the CDRouter test case(s) to run. Defaults to the CDROUTER_TESTS environment variable.
           TicketKey (str): The ticket key to associate with the test results. Defaults to the TICKET_KEY environment variable.
           tags (str): The tags to associate with the test results. Defaults to the TAGS environment variable.
           cdrouter_skipUpload (str): Whether to skip uploading test results to the CDRouter web UI. Defaults to the CDROUTER_SKIP_UPLOAD environment variable.
           cdrouter_message (str): The message to associate with the test results. Defaults to the CDROUTER_MESSAGE environment variable.

       Returns:
           Tuple of stdout and stderr from the subprocess run command.
   """
    cmd = f'java -jar %userprofile%\bin\jenkins-cli.jar -s {jenkins_url} -webSocket -auth "{username}":"{api_token}" '
    cmd += f'build "{job_name}" -v '
    cmd += f'-p testkit_debug="{testkit_debug}" '
    cmd += f'-p cdrouter_restart="{cdrouter_restart}" '
    cmd += f'-p cdrouter_device="{cdrouter_device}" '
    cmd += f'-p cdrouter_config="{cdrouter_config}" '
    cmd += f'-p cdrouter_package="{cdrouter_package}" '
    cmd += f'-p cdrouter_test="{cdrouter_test}" '
    cmd += f'-p cdrouter_tests="{cdrouter_tests}" '
    cmd += f'-p TicketKey="{TicketKey}" '
    cmd += f'-p tags="{tags}" '
    cmd += f'-p cdrouter_skipUpload="{cdrouter_skipUpload}" '
    cmd += f'-p cdrouter_message="{cdrouter_message}"'

    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout, result.stderr
