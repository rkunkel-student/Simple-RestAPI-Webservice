#
"""
:author: Roland Kunkel
:date: 6/9/2019

main entry point for the SDET coding challenge.

Running out of time or I would have implemented better error handling and
logging.
"""
import xmltodict
from subprocess import check_call, CalledProcessError


class CriticalErrorsFound(BaseException):
    """Raised when deployment should be prevented"""
    pass


def parse_xml_report(report):
    """ This could be cleaned ... """
    try:
        with open(report) as fp:
            doc = xmltodict.parse(fp.read())
            critical_failures = doc['robot']['statistics']['total']['stat'][0]['@fail']  # block deployment if not 0
            total_failures = doc['robot']['statistics']['total']['stat'][1]['@fail']
            total_tests = str(int(doc['robot']['statistics']['total']['stat'][1]['@pass']) + int(total_failures))
            print(
                "Total Tests: {}\nTotal Failures: {}\nCritical Failures: {}".format(
                    total_tests, total_failures, critical_failures
                ))
            if critical_failures != '0':
                print("Failing Status for: {}".format(report))
                raise CriticalErrorsFound
            print("Passing Status for: {}".format(report))
    except CriticalErrorsFound:
        raise


if __name__ == '__main__':
    """
        I provided a positive and negative test suite to show deploy / don't 
        deploy logic.
    """

    try:
        check_call(['robot', '--report', 'pos-report.html', '--output', 'pos-output.xml', '--critical', 'coding-challenge', 'webservice_tests.robot'], shell=True)
        check_call(['robot', '--report', 'neg-report.html', '--output', 'neg-output.xml', '--critical', 'coding-challenge', 'webservice_tests_2.robot'], shell=True)

    except CalledProcessError:
        # logger.exception( ... )
        # Prevent Deployment
        pass

    print('------------------------------')

    try:
        parse_xml_report('pos-output.xml')
        print("Deployment to jenkins approved")

    except CriticalErrorsFound:
        # logger.exception( ... )
        print("Critical Errors were found while running the test suite")
        print("Preventing deployment to jenkins")

    print('------------------------------')

    try:
        parse_xml_report('neg-output.xml')
        print("Deployment to jenkins approved")

    except CriticalErrorsFound:
        # logger.exception( ... )
        print("Critical Errors were found while running the test suite")
        print("Preventing deployment to jenkins")