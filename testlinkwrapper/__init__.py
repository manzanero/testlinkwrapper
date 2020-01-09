import datetime
import os
import xml
from typing import List

import testlink
import json
import logging


class BaseTestLinkWrapperOcject(object):
    def __repr__(self):
        return json.dumps(self.__dict__)


class TestProject(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict):
        self.id: str = response_dict['id']
        self.notes: str = response_dict['notes']
        self.color: str = response_dict['color']
        self.active: bool = bool(int(response_dict['active']))
        self.option_reqs: bool = bool(int(response_dict['option_reqs']))
        self.option_priority: bool = bool(int(response_dict['option_priority']))
        self.option_automation = bool(int(response_dict['option_automation']))
        self.options: str = response_dict['options']
        self.prefix: str = response_dict['prefix']
        self.tc_counter: bool = bool(int(response_dict['tc_counter']))
        self.is_public: bool = bool(int(response_dict['is_public']))
        self.issue_tracker_enabled: bool = bool(int(response_dict['issue_tracker_enabled']))
        self.reqmgr_integration_enabled: bool = bool(int(response_dict['reqmgr_integration_enabled']))
        self.api_key: str = response_dict['api_key']
        self.name: str = response_dict['name']
        self.opt: str = response_dict['opt']
        self.automationEnabled: bool = bool(int(response_dict['opt']['automationEnabled']))
        self.inventoryEnabled: bool = bool(int(response_dict['opt']['inventoryEnabled']))
        self.requirementsEnabled: bool = bool(int(response_dict['opt']['requirementsEnabled']))
        self.testPriorityEnabled: bool = bool(int(response_dict['opt']['testPriorityEnabled']))
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class TestPlan(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict):
        self.active: bool = bool(int(response_dict['active']))
        self.api_key: str = response_dict['api_key']
        self.id: str = response_dict['id']
        self.is_open: bool = bool(int(response_dict['is_open']))
        self.is_public: bool = bool(int(response_dict['is_public']))
        self.name: str = response_dict['name']
        self.notes: str = response_dict['notes']
        self.testproject_id: str = response_dict['testproject_id']
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class TestSuite(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict):
        self.id: str = response_dict['id']
        self.details: str = response_dict['details']
        self.name: str = response_dict['name']
        self.node_type_id: str = response_dict['node_type_id']
        self.node_order: str = response_dict['node_order']
        self.parent_id: str = response_dict['parent_id']
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class Build(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict):
        self.id: str = response_dict['id']
        self.testplan_id: str = response_dict['testplan_id']
        self.name: str = response_dict['name']
        self.notes: str = response_dict['notes']
        self.active: bool = bool(int(response_dict['active']))
        self.is_open: bool = bool(int(response_dict['is_open']))
        self.release_date: str = response_dict['release_date']
        self.closed_on_date: str = response_dict['closed_on_date']
        self.creation_ts: str = response_dict['creation_ts']
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class Step(BaseTestLinkWrapperOcject):
    def __init__(self, step_number: int, actions: str, expected_results: str, execution_type: int):
        self.step_number = step_number
        self.actions = actions
        self.expected_results = expected_results
        self.execution_type = execution_type


class TestCase(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict: dict):
        self.id: str = response_dict.get('testcase_id', response_dict['id'])
        self.parent_id: str = response_dict.get('parent_id', response_dict.get('testsuite_id'))
        self.node_type_id: str = response_dict.get('node_type_id')
        self.node_order: int = int(response_dict['node_order'])
        self.node_table: str = response_dict.get('node_table')
        self.name: str = response_dict['name']
        self.external_id: str = response_dict.get('external_id', response_dict.get('tc_external_id'))
        self.version: int = int(response_dict['version'])
        self.layout: str = response_dict['layout']
        self.status: str = str(response_dict['status'])
        self.summary: str = response_dict['summary']
        self.preconditions: str = response_dict['preconditions']
        self.importance: int = int(response_dict['importance'])
        self.author_id: str = response_dict['author_id']
        self.creation_ts: str = response_dict['creation_ts']
        self.updater_id: str = response_dict['updater_id']
        self.modification_ts: str = response_dict['modification_ts']
        self.active: bool = bool(int(response_dict['active']))
        self.is_open: bool = bool(int(response_dict['is_open']))
        self.execution_type: int = int(response_dict['execution_type'])
        self.estimated_exec_duration: str = response_dict['estimated_exec_duration']
        self.steps: list = response_dict['steps']


class StepResult(BaseTestLinkWrapperOcject):
    def __init__(self, step_number: int, result: str, notes: str):
        self.step_number = step_number
        self.result = result
        self.notes = notes
        assert result in Result.values()


class TestCaseResultReport(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict: dict):
        self.id: str = response_dict['id']
        self.build_id: str = response_dict['build_id']
        self.tester_id: str = response_dict['tester_id']
        self.execution_ts: str = response_dict['execution_ts']
        self.status: str = response_dict['status']
        self.testplan_id: str = response_dict['testplan_id']
        self.tcversion_id: str = response_dict['tcversion_id']
        self.tcversion_number: int = int(response_dict['tcversion_number'])
        self.platform_id: str = response_dict['platform_id']
        self.execution_type: str = response_dict['execution_type']
        self.execution_duration: str = response_dict['execution_duration']
        self.notes: str = response_dict['notes']
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class Attachment(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict: dict):
        self.id: str = response_dict['fk_id']
        self.fk_id: str = response_dict['fk_id']
        self.fk_table: str = response_dict['fk_table']
        self.title: str = response_dict['title']
        self.description: str = response_dict['description']
        self.file_name: str = response_dict['file_name']
        self.file_size: int = int(response_dict['file_size'])
        self.file_type: str = response_dict['file_type']


class Platform(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict: dict):
        self.id: str = response_dict['id']
        self.name: str = response_dict['name']
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class User(BaseTestLinkWrapperOcject):
    def __init__(self, response_dict: dict):
        self.id: str = response_dict['user_id']
        self.user_id: str = response_dict['user_id']
        self.name: str = response_dict['login']
        self.login: str = response_dict['login']
        self.first: str = response_dict['first']
        self.last: str = response_dict['last']
        assert all(x in self.__dict__.keys() for x in response_dict.keys())


class ConstansObject(object):
    @classmethod
    def values(cls):
        return list(cls.__dict__.values())

    @classmethod
    def parse(cls, value):
        return {v: k for k, v in cls.__dict__.items()}[value].lower()


class ExecutionType(ConstansObject):
    MANUAL = 1
    AUTOMATED = 2


class StepStatus(ConstansObject):
    DRAFT = 1
    READY_FOR_REVIEW = 2
    REVIEW_IN_PROGRESS = 3
    REWORK = 4
    OBSOLETE = 5
    FUTURE = 6
    FINAL = 7


class Importance(ConstansObject):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class ResponseDetails(ConstansObject):
    FULL = 'full'
    SIMPLE = 'simple'
    VALUE = 'value'


class Result(ConstansObject):
    PASS = 'p'
    FAIL = 'f'
    BLOCKED = 'b'
    INCOMPLETE = 'c'
    NOT_APLICABLE = 'd'
    KNOWN_INCIDENT = 'k'


class ActionOnDuplicate(ConstansObject):
    BLOCK = 'block'
    GENERATE_NEW = 'generate_new'
    CREATE_NEW_VERSION = 'create_new_version'


class TestLinkWrapper(object):

    def __init__(self, server_url, devkey):
        self.client: testlink.TestlinkAPIClient = testlink.TestlinkAPIClient(server_url, devkey)

    @property
    def projects(self):
        return [TestProject(x) for x in self.client.getProjects()]

    def create_test_project(self, name: str, prefix: str, notes: str, active: bool = True, public: bool = True,
                            requirements_enabled: bool = True, test_priority_enabled: bool = True,
                            automation_enabled: bool = True, inventory_enabled: bool = True) -> TestProject:
        response = self.client.createTestProject(
            testprojectname=name,
            testcaseprefix=prefix,
            notes=notes,
            active=1 if active else 0,
            public=1 if public else 0,
            options={'requirementsEnabled': 1 if requirements_enabled else 0,
                     'testPriorityEnabled': 1 if test_priority_enabled else 0,
                     'automationEnabled': 1 if automation_enabled else 0,
                     'inventoryEnabled': 1 if inventory_enabled else 0},
            itsname=1,
            itsenabled=1
        )
        assert response[0]['status'], "error on test project creation: " + str(response)
        return self.get_test_project(name=name)

    # def delete_test_project(self, prefix):
    #     old_project = self.client.deleteTestProject(
    #         prefix=prefix,
    #     )
    #     assert old_project['status']
    #     return old_project

    def get_test_project_id_by_node_id(self, node_id: str) -> str:
        return self.client.getProjectIDByNode(node_id)

    def get_test_project(self, name: str) -> TestProject:
        response = self.client.getTestProjectByName(name)
        assert response['name'] == name, "error on test project search: " + str(response)
        return TestProject(response)

    def create_test_plan(self, name: str, test_project: TestProject,
                         notes: str, active: bool = True, public: bool = True) -> TestPlan:
        response = self.client.createTestPlan(
            testplanname=name,
            testprojectname=test_project.name,
            notes=notes,
            active=1 if active else 0,
            public=1 if public else 0
        )
        assert response[0]['status'], "error on test plan creation: " + str(response)
        return self.get_test_plan(name=name, test_project=test_project)

    def get_test_plan(self, name: str, test_project: TestProject) -> TestPlan:
        response = self.client.getTestPlanByName(test_project.name, name)
        assert response[0]['name'] == name, "error on test plan search: " + str(response)
        return TestPlan(response[0])

    def get_test_plans_for_test_project(self, test_project: TestProject) -> List[TestPlan]:
        test_plans = self.client.getProjectTestPlans(test_project.id)
        return [self.get_test_plan(test_plan['name'], test_project) for test_plan in test_plans]

    def delete_test_plan(self, test_plan: TestPlan) -> TestPlan:
        response = self.client.deleteTestPlan(testplanid=test_plan.id)
        assert response[0]['status'], "error on test plan deletion: " + str(response)
        return test_plan

    def create_test_suite(self, name: str, test_project: TestProject, test_suite: TestSuite = None,
                          details: str = '', order: int = 0, check_duplicated_name: bool = True,
                          action_on_duplicated_name: str = ActionOnDuplicate.BLOCK) -> TestSuite:
        response = self.client.createTestSuite(
            testprojectid=test_project.id,
            parentid=test_suite.id,  # untested
            testsuitename=name,
            details=details,
            order=order,
            checkduplicatedname=1 if check_duplicated_name else 0,
            actiononduplicatedname=action_on_duplicated_name
        )
        try:
            assert response[0]['status'], "error on test suite creation: " + str(response)
        except KeyError:
            raise testlink.TestLinkError(response['msg'])
        return self.get_test_suite_by_id(response[0]['id'])

    def get_test_suite_by_id(self, test_suite_id: str) -> TestSuite:
        response = self.client.getTestSuiteByID(test_suite_id)
        assert response['id'] == test_suite_id, "error on test suite search: " + str(response)
        return TestSuite(response)

    def get_test_suites_for_test_suite(self, test_suite_id: str) -> List[TestSuite]:
        response = self.client.getTestSuitesForTestSuite(test_suite_id)
        if not response:
            return []
        return [TestSuite(response)] if 'id' in response else [TestSuite(ts) for ts in response.values()]

    def get_test_suite_by_path(self, path: str, test_project: TestProject, test_suite: TestSuite = None) -> TestSuite:
        ts_folders = [x for x in path.split('/') if x]
        for ts_folder in ts_folders:
            test_suite = self.get_test_suite(name=ts_folder, test_project=test_project, test_suite=test_suite)
        return test_suite

    def get_test_suite(self, name: str, test_project: TestProject, test_suite: TestSuite = None) -> TestSuite:
        if test_suite:
            try:
                ts_for_ts = self.get_test_suites_for_test_suite(test_suite.id)
                ts = [x for x in ts_for_ts if x.name == name][0]
            except (IndexError, testlink.TestLinkError):
                raise testlink.TestLinkError(f"Test Suite (name={name}) does not exist on "
                                             f"Test Suite (name={test_suite.name})")
            return ts
        else:
            try:
                first_level_ts_for_tp = self.client.getFirstLevelTestSuitesForTestProject(test_project.id)
                ts = [x for x in first_level_ts_for_tp if x['name'] == name][0]
            except (IndexError, testlink.TestLinkError):
                raise testlink.TestLinkError(f"Test Suite (name={name}) does not exist on "
                                             f"Test Project (name={test_project.name})")
            return self.get_test_suite_by_id(test_suite_id=ts['id'])

    # api dont support this method
    # def update_test_suite(self, name: str, test_project: TestProject, details: str, order: int = 0) -> TestSuite:

    def create_build(self, name: str, test_plan: TestPlan, notes: str, active: bool = True,
                     is_open: bool = True, release_date: datetime = None,
                     copy_testers_from_build: bool = False) -> Build:
        response = self.client.createBuild(
            testplanid=test_plan.id,
            buildname=name,
            buildnotes=notes,
            active=1 if active else 0,
            open=1 if is_open else 0,
            releasedate=(release_date or datetime.datetime.now()).strftime('%Y-%m-%d'),
            copytestersfrombuild=copy_testers_from_build
        )
        if not response[0]['status']:
            raise testlink.TestLinkError(response[0]['message'])
        return self.get_build(name=name, test_plan=test_plan)

    def get_build(self, name: str, test_plan: TestPlan) -> Build:
        b_for_tp = self.client.getBuildsForTestPlan(test_plan.id)
        try:
            return Build([x for x in b_for_tp if x['name'] == name][0])
        except IndexError:
            raise testlink.TestLinkError(f"Test Suite (name={name}) does not exist on "
                                         f"Test Plan (name={test_plan.name})")

    def create_test_case(self, name: str, test_suite: TestSuite, author: str, summary: str,
                         steps: list = None, preconditions: str = None, importance: Importance = None,
                         execution_type: ExecutionType = None, order: str = None, internal_id: str = None,
                         check_duplicated_name: bool = True, action_on_duplicated_name: str = ActionOnDuplicate.BLOCK,
                         status: str = None, estimated_exec_duration: float = None) -> TestCase:
        if not isinstance(steps[0], Step):
            steps = [Step(x['step_number'], x['actions'], x['expected_results'], x['execution_type']) for x in steps]
        steps = [x.__dict__ for x in steps]
        response = self.client.createTestCase(
            testcasename=name,
            testsuiteid=test_suite.id,
            testprojectid=self.get_test_project_id_by_node_id(test_suite.id),
            authorlogin=author,
            summary=summary,
            steps=steps,
            preconditions=preconditions,
            importance=importance,
            executiontype=execution_type,
            order=order,
            internalid=internal_id,
            checkduplicatedname=1 if check_duplicated_name else 0,
            actiononduplicatedname=action_on_duplicated_name,
            status=status,
            estimatedexecduration=estimated_exec_duration
        )
        assert response[0]['status'], "error on test case creation: " + str(response)
        if response[0]['additionalInfo']['has_duplicate'] and action_on_duplicated_name == ActionOnDuplicate.BLOCK:
            raise testlink.TestLinkError(f'test case (name={name}) already exist')
        return self.get_test_case(name=name, test_suite=test_suite)

    def get_test_case(self, name: str, test_suite: TestSuite) -> TestCase:
        tc_for_ts = self.client.getTestCasesForTestSuite(test_suite.id, True, ResponseDetails.FULL)
        try:
            return TestCase([x for x in tc_for_ts if x['name'] == name][0])
        except IndexError:
            raise testlink.testlinkerrors.TestLinkError(f"Test Case (name={name}) does not exist on "
                                                        f"Test Suite (name={test_suite.name})")

    def get_test_cases_for_test_suite(self, test_suite: TestSuite) -> List[TestCase]:
        tc_for_ts = self.client.getTestCasesForTestSuite(test_suite.id, True, ResponseDetails.FULL)
        return [TestCase(x[0]) for x in tc_for_ts]

    def get_test_cases_for_test_plan(self, test_plan: TestPlan) -> List[TestCase]:
        tc_for_tp = self.client.getTestCasesForTestPlan(test_plan.id, details=ResponseDetails.FULL)
        return [TestCase(self.client.getTestCase(x)[0]) for x in tc_for_tp.keys()]

    def get_platform(self, name, test_project: TestProject):
        response = self.client.getProjectPlatforms(testprojectid=test_project.id)
        try:
            return Platform(response[name])
        except KeyError:
            raise testlink.testlinkerrors.TestLinkError(f"The platform (name={name}) does not exits on "
                                                        f"Test Project (name={test_project.name})")

    def add_test_case_to_test_plan(self, test_plan: TestPlan, test_case: TestCase,
                                   version: int = None, platform: Platform = None, execution_order: str = None,
                                   urgency: str = None, overwrite: bool = False):
        test_project_id = self.get_test_project_id_by_node_id(test_case.parent_id)
        try:
            response = self.client.addTestCaseToTestPlan(
                testprojectid=test_project_id,
                testplanid=test_plan.id,
                testcaseexternalid=test_case.external_id,
                version=version or test_case.version,
                platformid=platform.id if platform else None,
                executionorder=execution_order,
                urgency=urgency,
                overwrite=1 if overwrite else 0
            )
        except xml.parsers.expat.ExpatError:
            raise testlink.testlinkerrors.TestLinkError(f"Test Case (name={test_case.name}) can't be moved")
        assert response['status'], "error attaching test case to test plan: " + str(response)

    def assign_test_case_to_user(self, name, test_plan: TestPlan, test_case: TestCase, build: Build,
                                 platform: Platform = None):
        response = self.client.assignTestCaseExecutionTask(
            user=name,
            testplanid=test_plan.id,
            testcaseexternalid=test_case.external_id,
            buildid=build.id,
            platformid=platform.id if platform else None,
        )
        assert response['status'], "error assign test case to user: " + response

    def get_user_assigned_to_test_case(self, test_plan: TestPlan, test_case: TestCase, build: Build,
                                       platform: Platform = None) -> [User, None]:
        response = self.client.getTestCaseAssignedTester(
            testplanid=test_plan.id,
            testcaseexternalid=test_case.external_id,
            buildid=build.id,
            platformid=platform.id if platform else None,
        )
        if response[0]['user_id'] == '':
            return None
        else:
            return User(response[0])

    def revoke_test_case_to_user(self, name, test_plan: TestPlan, test_case: TestCase, build: Build,
                                 platform: Platform = None):
        response = self.client.unassignTestCaseExecutionTask(
            testplanid=test_plan.id,
            testcaseexternalid=test_case.external_id,
            buildid=build.id,
            platformid=platform.id if platform else None,
            user=name,
        )
        assert response['status'], "error unassigning user from test case: " + str(response)

    def revoke_test_case_to_all_users(self, test_plan: TestPlan, test_case: TestCase, build: Build,
                                      platform: Platform = None):
        user = tls.get_user_assigned_to_test_case(test_plan, test_case, build, platform)
        while user:
            user = tls.get_user_assigned_to_test_case(test_plan, test_case, build, platform)
            if user:
                self.revoke_test_case_to_user(user.name, test_plan, test_case, build, platform)
            else:
                return

    def add_test_case_to_test_suite(self, test_case: TestCase, test_suite: TestSuite):
        response = self.client.setTestCaseTestSuite(testcaseexternalid=test_case.external_id, testsuiteid=test_suite.id)
        assert response[0]['status'], "error attaching test case to test suite: " + str(response)

    def create_test_case_result_report(self, result: str, test_plan: TestPlan, test_case: TestCase,
                                       build: Build, user_name: str, notes: str = None,
                                       execution_duration: float = 0, timestamp: datetime = datetime.datetime.now(),
                                       steps_result: list = None, platform: Platform = None) -> TestCaseResultReport:
        notes = (notes + '\n\n' if notes else '') + \
                'execution duration: {:.1f} s.\n'.format(execution_duration if execution_duration else 0) + \
                'Test Case version: %s' % test_case.version

        if steps_result:
            if not isinstance(steps_result[0], StepResult):
                steps_result = [StepResult(s['step_number'], s['result'], s['notes']) for s in steps_result]
            steps_result = [x.__dict__ for x in steps_result]
            for step_result in steps_result:
                notes = notes + '\n%s - %s - %s' \
                        % (step_result['step_number'], Result.parse(step_result['result']), step_result['notes'])

        response = self.client.reportTCResult(
            testplanid=test_plan.id,
            status=result,
            testcaseid=test_case.id,
            # testcaseexternalid=test_case.external_id,
            buildid=build.id,
            # buildname=build.name,
            # platformid=None,
            platformname=platform.name if platform else None,
            notes=notes,
            # guess=1,
            # bugid=None,
            # customfields=None,
            # overwrite=False,
            user=user_name,
            execduration=execution_duration,
            timestamp=timestamp.strftime('%Y-%m-%d %H:%M:%S') if timestamp else None,
            steps=steps_result
        )
        assert response[0]['status'], "error on test case result report creation: " + str(response)
        return self.get_last_test_case_result_report(test_plan=test_plan, build=build, test_case=test_case)

    def add_attachment_to_test_item(self, test_item: any, path: str, name: str = None):
        if isinstance(test_item, TestCaseResultReport):
            response = self.client.uploadExecutionAttachment(
                executionid=test_item.id,
                attachmentfile=path,
                filename=name,
                filetype=None
            )
        else:
            raise AssertionError("%s can't have attachements" % test_item.name)
        assert response['file_name'] == name, "error attaching item to test case: " + str(response)
        return Attachment(response)

    def get_last_test_case_result_report(self, test_plan: TestPlan, build: Build,
                                         test_case: TestCase) -> TestCaseResultReport:
        response = self.client.getLastExecutionResult(
            testplanid=test_plan.id,
            buildid=build.id,
            testcaseid=test_case.id)
        if response == [{'id': -1}]:
            raise testlink.TestLinkError(f'test case (name={test_case.name}) not executed yet')
        assert response[0]['testplan_id'] == test_plan.id, "error on test case result report search: " + str(response)
        return TestCaseResultReport(response[0])

    def delete_last_test_case_result_report(self, test_plan: TestPlan, build: Build,
                                            test_case: TestCase) -> TestCaseResultReport:
        response = self.get_last_test_case_result_report(test_plan=test_plan, build=build, test_case=test_case)
        self.client.deleteExecution(int(response.id))
        return response

    def result_report(self,
                      test_project_name: str,
                      test_project_prefix: str = None,
                      test_project_notes: str = None,
                      test_suite_name: str = None,
                      test_suite_base: str = None,
                      test_suite_details: str = None,
                      test_case_name: str = None,
                      test_case_author: str = None,
                      test_case_summary: str = None,
                      test_case_steps=None,
                      test_plan_name: str = None,
                      platform_name: str = None,
                      test_plan_notes: str = None,
                      build_name: str = None,
                      build_notes: str = None,
                      test_case_result=None,
                      user_name=None,
                      test_case_result_report_attachement: [list, str] = None,
                      test_case_result_report_notes=None,
                      execution_duration=None,
                      step_results=None,
                      delete_last_test_case_result_report=None,
                      create_test_project_if_not_exists=False,
                      create_test_suite_if_not_exists=False,
                      create_test_case_if_not_exists=False,
                      create_new_version_of_test_case_if_exists=False,
                      create_test_plan_if_not_exists=False,
                      create_build_if_not_exists=False, ):
        tl = self

        # Test Project
        try:
            p = tl.get_test_project(name=test_project_name)
            logging.info('Test Project: {}'.format(p))
        except testlink.TestLinkError:
            if create_test_project_if_not_exists:
                p = tl.create_test_project(name=test_project_name, prefix=test_project_prefix, notes=test_project_notes)
                logging.info('created Test Project: {}'.format(p))
            else:
                raise

        # Test Suite
        ts = None
        if test_suite_base:
            ts = tl.get_test_suite_by_path(path=test_suite_base, test_project=p)
        try:
            ts = tl.get_test_suite(name=test_suite_name, test_project=p, test_suite=ts)
            logging.info('Test Suite: {}'.format(ts))
        except testlink.TestLinkError:
            if create_test_suite_if_not_exists:
                ts = tl.create_test_suite(name=test_suite_name, test_project=p, test_suite=ts,
                                          details=test_suite_details)
                logging.info('created Test Suite: {}'.format(ts))
            else:
                raise

        # Test Case
        try:
            tc = tl.get_test_case(name=test_case_name, test_suite=ts)
            if create_new_version_of_test_case_if_exists:
                tc = tl.create_test_case(name=test_case_name, test_suite=ts, author=test_case_author,
                                         summary=test_case_summary, steps=test_case_steps,
                                         action_on_duplicated_name=ActionOnDuplicate.CREATE_NEW_VERSION)
                logging.info(f'created new version of Test Case: {tc}')
            else:
                logging.info(f'Test Case: {tc}')
        except testlink.TestLinkError:
            if create_test_case_if_not_exists:
                assert test_case_author, "Parameter test_case_author is required, but has not been provided"
                assert test_case_summary, "Parameter test_case_summary is required, but has not been provided"
                assert test_case_steps, "Parameter test_case_steps is required, but has not been provided"
                tc = tl.create_test_case(name=test_case_name, test_suite=ts, author=test_case_author,
                                         summary=test_case_summary, steps=test_case_steps,
                                         action_on_duplicated_name=ActionOnDuplicate.BLOCK)
                logging.info(f'created Test Case: {tc}')
            else:
                raise

        # Test Plan
        try:
            tp = tl.get_test_plan(name=test_plan_name, test_project=p)
            logging.info(f'Test Plan: {tp}')
        except testlink.TestLinkError:
            if create_test_plan_if_not_exists:
                tp = tl.create_test_plan(name=test_plan_name, test_project=p, notes=test_plan_notes)
                logging.info(f'created Test Plan: {tp}')
            else:
                raise

        # # delete_test_plan = True
        # delete_test_plan = False
        # if delete_test_plan:
        #     tp = tl.delete_test_plan(test_plan=tp)
        #     print('deleted tp:', tp)
        #     exit()

        # Build
        try:
            b = tl.get_build(name=build_name, test_plan=tp)
            logging.info(f'Build: {b}')
        except testlink.TestLinkError:
            if create_build_if_not_exists:
                b = tl.create_build(name=build_name, test_plan=tp, notes=build_notes)
                logging.info(f'created Build: {b}')
            else:
                raise

        # Platform
        if platform_name:
            pl = tl.get_platform(name=platform_name, test_project=p)
            logging.info(f'Platform: {pl}')
        else:
            pl = None
            logging.debug('Test Project has no platforms')
            # platforms = list(tl.client.getProjectPlatforms(testprojectid=p.id).keys())
            # if platforms:
            #     pl = tl.get_platform(name=platforms[0], test_project=p)
            #     logging.info('Platform: {}'.format(pl))
            # else:
            #     pl = None
            #     logging.debug('Test Project has no platforms')

        try:
            tl.add_test_case_to_test_plan(test_plan=tp, test_case=tc, platform=pl, overwrite=True)
        except testlink.TestLinkError:
            assert tc.id in tl.client.getTestCasesForTestPlan(testplanid=tp.id), \
                f"Test Case (name={tc.name}) not in Test Plan (name={tp.name})"

        # try:
        #     tl.update_test_case_version(test_plan=tp, test_case=tc)
        # except testlink.TestLinkError:
        #     assert tc.id in tl.client.getTestCasesForTestPlan(testplanid=tp.id), \
        #         "Test Case (name: %s) not in Test Plan (name: %s)" % (tc.name, tp.name)

        # Assigned user
        if not tl.get_user_assigned_to_test_case(test_plan=tp, test_case=tc, build=b, platform=pl):
            tl.assign_test_case_to_user('Testing_Office', test_plan=tp, test_case=tc, build=b, platform=pl)
            logging.info("Test Case assigned to 'Testing_Office'")

        # Test Case Result Report
        try:
            r = tl.create_test_case_result_report(result=test_case_result, test_plan=tp, test_case=tc, build=b,
                                                  user_name=user_name, notes=test_case_result_report_notes,
                                                  execution_duration=execution_duration, steps_result=step_results,
                                                  platform=pl)
            logging.info(f'created Test Case Result Report: {r}')
        except testlink.TestLinkError:
            r = tl.get_last_test_case_result_report(test_plan=tp, build=b, test_case=tc)
            logging.info(f'Test Case Result Report: {r}')

        if test_case_result_report_attachement:
            tcrras = test_case_result_report_attachement
            tcrras = tcrras if isinstance(tcrras, list) else [tcrras]
            for tcrra in tcrras:
                if os.path.exists(tcrra):
                    a = tl.add_attachment_to_test_item(test_item=r, path=tcrra, name=os.path.basename(tcrra))
                    logging.info(f'created Attachment: {a}')
                else:
                    logging.error(f'file (path: %s) don\'t exist: {tcrra}')

        if delete_last_test_case_result_report:
            r = tl.delete_last_test_case_result_report(test_plan=tp, build=b, test_case=tc)
            logging.info(f'deleted Test Case Result Report: {r}')


if __name__ == '__main__':
    SERVER_URL = 'http://xxx'
    DEVKEY = 'xxx'
    tl = TestLinkWrapper(SERVER_URL, DEVKEY)
    for p in tl.projects:
        print(p.name)
