import pytest
from src.interface.crawler.background.parser.iam_action_html_parser import (
    IAMActionHTMLParser,
)


def test_colspan_and_rowspan():
    html = """
    <table>
      <thead>
      <tr>
        <th>Actions</th>
        <th>Header 2</th>
        <th>Header 3</th>
      </thead>
      <tr>
        <td rowspan="2">A</td>
        <td>B</td>
        <td>C</td>
      </tr>
      <tr>
        <td colspan="2">D</td>
      </tr>
      <tr>
        <td>E</td>
        <td>F</td>
        <td>G</td>
      </tr>
    </table>
    """
    parser = IAMActionHTMLParser()
    parser.feed(html)
    assert parser.rows == [["A", "B", "C"], ["A", "D", "D"], ["E", "F", "G"]]


def test_complex_colspan_rowspan():
    html = """
    <table>
      <tr>
        <th>Action</th>
        <th>Header 2</th>
        <th>Header 3</th>
      </thead>
      <tr>
        <td rowspan="2" colspan="2">A</td>
        <td>B</td>
      </tr>
      <tr>
        <td>C</td>
      </tr>
      <tr>
        <td>D</td>
        <td>E</td>
        <td>F</td>
      </tr>
    </table>
    """
    parser = IAMActionHTMLParser()
    parser.feed(html)
    assert parser.rows == [["A", "A", "B"], ["A", "A", "C"], ["D", "E", "F"]]


def test_aws_action_list():
    html = """
              <table id="w44aab5b9d803c11c15">
                <thead>
                    <tr>
                        <th>Actions</th>
                        <th>Description</th>
                        <th>Access level</th>
                        <th>Resource types (*required)</th>
                        <th>Condition keys</th>
                        <th>Dependent actions</th>
                    </tr>
                </thead>
                    <tbody><tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-AssociateDirectory">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">AssociateDirectory</a>
                        </td>
                        <td tabindex="-1">Grants permission to connect a directory to be used by AWS IAM Identity Center</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                ds:AuthorizeApplication
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-AssociateProfile">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">AssociateProfile</a>
                        </td>
                        <td tabindex="-1">Grants permission to create an association between a directory user or group and a profile</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-AttachCustomerManagedPolicyReferenceToPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachCustomerManagedPolicyReferenceToPermissionSet.html">AttachCustomerManagedPolicyReferenceToPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to attach a customer managed policy reference to a permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-AttachManagedPolicyToPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AttachManagedPolicyToPermissionSet.html">AttachManagedPolicyToPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to attach an AWS managed policy to a permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="3" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateAccountAssignment">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateAccountAssignment.html">CreateAccountAssignment</a>
                        </td>
                        <td rowspan="3" tabindex="-1">Grants permission to assign access to a Principal for a specified AWS account using a specified permission set</td>
                        <td rowspan="3" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Account">Account*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="3" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateApplication">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplication.html">CreateApplication</a>
                        </td>
                        <td rowspan="3" tabindex="-1">Grants permission to create an application</td>
                        <td rowspan="3" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-ApplicationProvider">ApplicationProvider*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_RequestTag___TagKey_">aws:RequestTag/${TagKey}</a>
                            </p>
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_TagKeys">aws:TagKeys</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateApplicationAssignment">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateApplicationAssignment.html">CreateApplicationAssignment</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to create an application assignment</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateApplicationInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">CreateApplicationInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to add an application instance to AWS IAM Identity Center</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateApplicationInstanceCertificate">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">CreateApplicationInstanceCertificate</a>
                        </td>
                        <td tabindex="-1">Grants permission to add a new certificate for an application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateInstance.html">CreateInstance</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to create an identity center instance</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                iam:CreateServiceLinkedRole
                            </p>
                            <p>
                                organizations:DescribeOrganization
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_RequestTag___TagKey_">aws:RequestTag/${TagKey}</a>
                            </p>
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_TagKeys">aws:TagKeys</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateInstanceAccessControlAttributeConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateInstanceAccessControlAttributeConfiguration.html">CreateInstanceAccessControlAttributeConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to enable the instance for ABAC and specify the attributes</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                iam:AttachRolePolicy
                            </p>
                            <p>
                                iam:CreateRole
                            </p>
                            <p>
                                iam:DeleteRole
                            </p>
                            <p>
                                iam:DeleteRolePolicy
                            </p>
                            <p>
                                iam:DetachRolePolicy
                            </p>
                            <p>
                                iam:GetRole
                            </p>
                            <p>
                                iam:ListAttachedRolePolicies
                            </p>
                            <p>
                                iam:ListRolePolicies
                            </p>
                            <p>
                                iam:PutRolePolicy
                            </p>
                            <p>
                                iam:UpdateAssumeRolePolicy
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateManagedApplicationInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">CreateManagedApplicationInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to add a managed application instance to AWS IAM Identity Center</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="3" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreatePermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreatePermissionSet.html">CreatePermissionSet</a>
                        </td>
                        <td rowspan="3" tabindex="-1">Grants permission to create a permission set</td>
                        <td rowspan="3" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_RequestTag___TagKey_">aws:RequestTag/${TagKey}</a>
                            </p>
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_TagKeys">aws:TagKeys</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateProfile">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">CreateProfile</a>
                        </td>
                        <td tabindex="-1">Grants permission to create a profile for an application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateTrust">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">CreateTrust</a>
                        </td>
                        <td tabindex="-1">Grants permission to create a federation trust in a target account</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-CreateTrustedTokenIssuer">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_CreateTrustedTokenIssuer.html">CreateTrustedTokenIssuer</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to create a trusted token issuer for an instance</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_RequestTag___TagKey_">aws:RequestTag/${TagKey}</a>
                            </p>
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_TagKeys">aws:TagKeys</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="3" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteAccountAssignment">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteAccountAssignment.html">DeleteAccountAssignment</a>
                        </td>
                        <td rowspan="3" tabindex="-1">Grants permission to delete a Principal's access from a specified AWS account using a specified permission set</td>
                        <td rowspan="3" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Account">Account*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplication">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplication.html">DeleteApplication</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplicationAccessScope">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAccessScope.html">DeleteApplicationAccessScope</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete an access scope to an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplicationAssignment">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAssignment.html">DeleteApplicationAssignment</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete an application assignment</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplicationAuthenticationMethod">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationAuthenticationMethod.html">DeleteApplicationAuthenticationMethod</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete an authentication method to an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplicationGrant">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteApplicationGrant.html">DeleteApplicationGrant</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete a grant from an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplicationInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DeleteApplicationInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete the application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteApplicationInstanceCertificate">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DeleteApplicationInstanceCertificate</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete an inactive or expired certificate from the application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteInlinePolicyFromPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInlinePolicyFromPermissionSet.html">DeleteInlinePolicyFromPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete the inline policy from a specified permission set</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInstance.html">DeleteInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete an identity center instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteInstanceAccessControlAttributeConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteInstanceAccessControlAttributeConfiguration.html">DeleteInstanceAccessControlAttributeConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to disable ABAC and remove the attributes list for the instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteManagedApplicationInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DeleteManagedApplicationInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete the managed application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeletePermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeletePermissionSet.html">DeletePermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to delete a permission set</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeletePermissionsBoundaryFromPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeletePermissionsBoundaryFromPermissionSet.html">DeletePermissionsBoundaryFromPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to remove permissions boundary from a permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeletePermissionsPolicy">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DeletePermissionsPolicy</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete the permission policy associated with a permission set</td>
                        <td tabindex="-1">Permissions management</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteProfile">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DeleteProfile</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete the profile for an application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DeleteTrustedTokenIssuer">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DeleteTrustedTokenIssuer.html">DeleteTrustedTokenIssuer</a>
                        </td>
                        <td tabindex="-1">Grants permission to delete a trusted token issuer for an instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-TrustedTokenIssuer">TrustedTokenIssuer*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeAccountAssignmentCreationStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentCreationStatus.html">DescribeAccountAssignmentCreationStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to describe the status of the assignment creation request</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeAccountAssignmentDeletionStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeAccountAssignmentDeletionStatus.html">DescribeAccountAssignmentDeletionStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to describe the status of an assignment deletion request</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeApplication">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplication.html">DescribeApplication</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to obtain information about an application</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeApplicationAssignment">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationAssignment.html">DescribeApplicationAssignment</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to retrieve an application assignment</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeApplicationProvider">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeApplicationProvider.html">DescribeApplicationProvider</a>
                        </td>
                        <td tabindex="-1">Grants permission to describe an application provider</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-ApplicationProvider">ApplicationProvider*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeDirectories">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DescribeDirectories</a>
                        </td>
                        <td tabindex="-1">Grants permission to obtain information about the directories for this account</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstance.html">DescribeInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to obtain information about an identity center instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeInstanceAccessControlAttributeConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeInstanceAccessControlAttributeConfiguration.html">DescribeInstanceAccessControlAttributeConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to get the list of attributes used by the instance for ABAC</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribePermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribePermissionSet.html">DescribePermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to describe a permission set</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribePermissionSetProvisioningStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribePermissionSetProvisioningStatus.html">DescribePermissionSetProvisioningStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to describe the status for the given Permission Set Provisioning request</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribePermissionsPolicies">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DescribePermissionsPolicies</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all the permissions policies associated with a permission set</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeRegisteredRegions">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DescribeRegisteredRegions</a>
                        </td>
                        <td tabindex="-1">Grants permission to obtain the regions where your organization has enabled AWS IAM Identity Center</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeTrustedTokenIssuer">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeTrustedTokenIssuer.html">DescribeTrustedTokenIssuer</a>
                        </td>
                        <td tabindex="-1">Grants permission to describe a trusted token issuer for an instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-TrustedTokenIssuer">TrustedTokenIssuer*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DescribeTrusts">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DescribeTrusts</a>
                        </td>
                        <td tabindex="-1">Grants permission to obtain information about the trust relationships for this account</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DetachCustomerManagedPolicyReferenceFromPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DetachCustomerManagedPolicyReferenceFromPermissionSet.html">DetachCustomerManagedPolicyReferenceFromPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to detach a customer managed policy reference from a permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DetachManagedPolicyFromPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DetachManagedPolicyFromPermissionSet.html">DetachManagedPolicyFromPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to detach the attached AWS managed policy from the specified permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DisassociateDirectory">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DisassociateDirectory</a>
                        </td>
                        <td tabindex="-1">Grants permission to disassociate a directory to be used by AWS IAM Identity Center</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                ds:UnauthorizeApplication
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-DisassociateProfile">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">DisassociateProfile</a>
                        </td>
                        <td tabindex="-1">Grants permission to disassociate a directory user or group from a profile</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetApplicationAccessScope">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAccessScope.html">GetApplicationAccessScope</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to get an access scope to an application</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetApplicationAssignmentConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAssignmentConfiguration.html">GetApplicationAssignmentConfiguration</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to read assignment configurations for an application</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetApplicationAuthenticationMethod">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationAuthenticationMethod.html">GetApplicationAuthenticationMethod</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to get an authentication method to an application</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetApplicationGrant">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetApplicationGrant.html">GetApplicationGrant</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to obtain details about a grant belonging to an application</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetApplicationInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetApplicationInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve details for an application instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetApplicationTemplate">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetApplicationTemplate</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve application template details</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetInlinePolicyForPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetInlinePolicyForPermissionSet.html">GetInlinePolicyForPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to obtain the inline policy assigned to the permission set</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetManagedApplicationInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetManagedApplicationInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve details for an application instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetMfaDeviceManagementForDirectory">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetMfaDeviceManagementForDirectory</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve Mfa Device Management settings for the directory</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetPermissionSet</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve details of a permission set</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetPermissionsBoundaryForPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_GetPermissionsBoundaryForPermissionSet.html">GetPermissionsBoundaryForPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to get permissions boundary for a permission set</td>
                        <td rowspan="2" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetPermissionsPolicy">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetPermissionsPolicy</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all permission policies associated with a permission set</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                sso:DescribePermissionsPolicies
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetProfile">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetProfile</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve a profile for an application instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetSSOStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetSSOStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to check if AWS IAM Identity Center is enabled</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetSharedSsoConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetSharedSsoConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve shared configuration for the current SSO instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetSsoConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetSsoConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve configuration for the current SSO instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-GetTrust">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">GetTrust</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve the federation trust in a target account</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ImportApplicationInstanceServiceProviderMetadata">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ImportApplicationInstanceServiceProviderMetadata</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the application instance by uploading an application SAML metadata file provided by the service provider</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListAccountAssignmentCreationStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentCreationStatus.html">ListAccountAssignmentCreationStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to list the status of the AWS account assignment creation requests for a specified SSO instance</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListAccountAssignmentDeletionStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentDeletionStatus.html">ListAccountAssignmentDeletionStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to list the status of the AWS account assignment deletion requests for a specified SSO instance</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="3" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListAccountAssignments">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignments.html">ListAccountAssignments</a>
                        </td>
                        <td rowspan="3" tabindex="-1">Grants permission to list the assignee of the specified AWS account with the specified permission set</td>
                        <td rowspan="3" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Account">Account*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListAccountAssignmentsForPrincipal">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountAssignmentsForPrincipal.html">ListAccountAssignmentsForPrincipal</a>
                        </td>
                        <td tabindex="-1">Grants permission to list accounts assigned to user or group</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListAccountsForProvisionedPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListAccountsForProvisionedPermissionSet.html">ListAccountsForProvisionedPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list all the AWS accounts where the specified permission set is provisioned</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationAccessScopes">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAccessScopes.html">ListApplicationAccessScopes</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list access scopes to an application</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationAssignments">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignments.html">ListApplicationAssignments</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list application assignments</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationAssignmentsForPrincipal">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAssignmentsForPrincipal.html">ListApplicationAssignmentsForPrincipal</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list applications assigned to user or group</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationAuthenticationMethods">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationAuthenticationMethods.html">ListApplicationAuthenticationMethods</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list authentication methods to an application</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationGrants">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationGrants.html">ListApplicationGrants</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list grants from an application</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationInstanceCertificates">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ListApplicationInstanceCertificates</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all of the certificates for a given application instance</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationInstances">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ListApplicationInstances</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all application instances</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                sso:GetApplicationInstance
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationProviders">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationProviders.html">ListApplicationProviders</a>
                        </td>
                        <td tabindex="-1">Grants permission to list application providers</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-ApplicationProvider">ApplicationProvider*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplicationTemplates">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ListApplicationTemplates</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all supported application templates</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                sso:GetApplicationTemplate
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListApplications">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplications.html">ListApplications</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all applications associated with the instance of IAM Identity Center</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListCustomerManagedPolicyReferencesInPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListCustomerManagedPolicyReferencesInPermissionSet.html">ListCustomerManagedPolicyReferencesInPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list the customer managed policy references that are attached to a permission set</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListDirectoryAssociations">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ListDirectoryAssociations</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve details about the directory connected to AWS IAM Identity Center</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListInstances">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListInstances.html">ListInstances</a>
                        </td>
                        <td tabindex="-1">Grants permission to list the SSO Instances that the caller has access to</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListManagedPoliciesInPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListManagedPoliciesInPermissionSet.html">ListManagedPoliciesInPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list the AWS managed policies that are attached to a specified permission set</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListPermissionSetProvisioningStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSetProvisioningStatus.html">ListPermissionSetProvisioningStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to list the status of the Permission Set Provisioning requests for a specified SSO instance</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListPermissionSets">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSets.html">ListPermissionSets</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all permission sets</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListPermissionSetsProvisionedToAccount">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListPermissionSetsProvisionedToAccount.html">ListPermissionSetsProvisionedToAccount</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to list all the permission sets that are provisioned to a specified AWS account</td>
                        <td rowspan="2" tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Account">Account*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListProfileAssociations">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ListProfileAssociations</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve the directory user or group associated with the profile</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListProfiles">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">ListProfiles</a>
                        </td>
                        <td tabindex="-1">Grants permission to retrieve all profiles for an application instance</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                sso:GetProfile
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td rowspan="4" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListTagsForResource">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a>
                        </td>
                        <td rowspan="4" tabindex="-1">Grants permission to list the tags that are attached to a specified resource</td>
                        <td rowspan="4" tabindex="-1">Read</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-TrustedTokenIssuer">TrustedTokenIssuer</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ListTrustedTokenIssuers">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListTrustedTokenIssuers.html">ListTrustedTokenIssuers</a>
                        </td>
                        <td tabindex="-1">Grants permission to list trusted token issuers for an instance</td>
                        <td tabindex="-1">List</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="3" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-ProvisionPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ProvisionPermissionSet.html">ProvisionPermissionSet</a>
                        </td>
                        <td rowspan="3" tabindex="-1">Grants permission to provision a specified permission set to the specified target</td>
                        <td rowspan="3" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Account">Account*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutApplicationAccessScope">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAccessScope.html">PutApplicationAccessScope</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to create/update an access scope to an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutApplicationAssignmentConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAssignmentConfiguration.html">PutApplicationAssignmentConfiguration</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to add assignment configurations to an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutApplicationAuthenticationMethod">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationAuthenticationMethod.html">PutApplicationAuthenticationMethod</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to create/update an authentication method to an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutApplicationGrant">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutApplicationGrant.html">PutApplicationGrant</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to create/update a grant to an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutInlinePolicyToPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutInlinePolicyToPermissionSet.html">PutInlinePolicyToPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to attach an IAM inline policy to a permission set</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutMfaDeviceManagementForDirectory">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">PutMfaDeviceManagementForDirectory</a>
                        </td>
                        <td tabindex="-1">Grants permission to put Mfa Device Management settings for the directory</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutPermissionsBoundaryToPermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_PutPermissionsBoundaryToPermissionSet.html">PutPermissionsBoundaryToPermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to add permissions boundary to a permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-PutPermissionsPolicy">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">PutPermissionsPolicy</a>
                        </td>
                        <td tabindex="-1">Grants permission to add a policy to a permission set</td>
                        <td tabindex="-1">Permissions management</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-SearchGroups">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">SearchGroups</a>
                        </td>
                        <td tabindex="-1">Grants permission to search for groups within the associated directory</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                ds:DescribeDirectories
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-SearchUsers">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">SearchUsers</a>
                        </td>
                        <td tabindex="-1">Grants permission to search for users within the associated directory</td>
                        <td tabindex="-1">Read</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                ds:DescribeDirectories
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-StartSSO">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">StartSSO</a>
                        </td>
                        <td tabindex="-1">Grants permission to initialize AWS IAM Identity Center</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                organizations:DescribeOrganization
                            </p>
                            <p>
                                organizations:EnableAWSServiceAccess
                            </p>
                        </td>
                    </tr>
                    <tr>
                        <td rowspan="5" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-TagResource">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TagResource.html">TagResource</a>
                        </td>
                        <td rowspan="5" tabindex="-1">Grants permission to associate a set of tags with a specified resource</td>
                        <td rowspan="5" tabindex="-1">Tagging</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-TrustedTokenIssuer">TrustedTokenIssuer</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_RequestTag___TagKey_">aws:RequestTag/${TagKey}</a>
                            </p>
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_TagKeys">aws:TagKeys</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="5" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UntagResource">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UntagResource.html">UntagResource</a>
                        </td>
                        <td rowspan="5" tabindex="-1">Grants permission to disassociate a set of tags from a specified resource</td>
                        <td rowspan="5" tabindex="-1">Tagging</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-TrustedTokenIssuer">TrustedTokenIssuer</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-aws_TagKeys">aws:TagKeys</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplication">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateApplication.html">UpdateApplication</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to update an application</td>
                        <td rowspan="2" tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Application">Application*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1"></td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-sso_ApplicationAccount">sso:ApplicationAccount</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceActiveCertificate">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceActiveCertificate</a>
                        </td>
                        <td tabindex="-1">Grants permission to set a certificate as the active one for this application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceDisplayData">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceDisplayData</a>
                        </td>
                        <td tabindex="-1">Grants permission to update display data of an application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceResponseConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceResponseConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to update federation response configuration for the application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceResponseSchemaConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceResponseSchemaConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to update federation response schema configuration for the application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceSecurityConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceSecurityConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to update security details for the application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceServiceProviderConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceServiceProviderConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to update service provider related configuration for the application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateApplicationInstanceStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateApplicationInstanceStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the status of an application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateDirectoryAssociation">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateDirectoryAssociation</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the user attribute mappings for your connected directory</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateInstance">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstance.html">UpdateInstance</a>
                        </td>
                        <td tabindex="-1">Grants permission to update an identity center instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateInstanceAccessControlAttributeConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateInstanceAccessControlAttributeConfiguration.html">UpdateInstanceAccessControlAttributeConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the attributes to use with the instance for ABAC</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateManagedApplicationInstanceStatus">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateManagedApplicationInstanceStatus</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the status of a managed application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td rowspan="2" tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdatePermissionSet">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdatePermissionSet.html">UpdatePermissionSet</a>
                        </td>
                        <td rowspan="2" tabindex="-1">Grants permission to update the permission set</td>
                        <td rowspan="2" tabindex="-1">Permissions management</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-Instance">Instance*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-PermissionSet">PermissionSet*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateProfile">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateProfile</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the profile for an application instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateSSOConfiguration">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateSSOConfiguration</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the configuration for the current SSO instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateTrust">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-using-id-policies.html#policyexample">UpdateTrust</a>
                        </td>
                        <td tabindex="-1">Grants permission to update the federation trust in a target account</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                    <tr>
                        <td tabindex="-1" id="awsiamidentitycentersuccessortoawssinglesign-on-UpdateTrustedTokenIssuer">
                             
                            <a href="https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_UpdateTrustedTokenIssuer.html">UpdateTrustedTokenIssuer</a>
                        </td>
                        <td tabindex="-1">Grants permission to update a trusted token issuer for an instance</td>
                        <td tabindex="-1">Write</td>
                        <td tabindex="-1">
                            <p>
                                <a href="#awsiamidentitycentersuccessortoawssinglesign-on-TrustedTokenIssuer">TrustedTokenIssuer*</a>
                            </p>
                        </td>
                        <td tabindex="-1"></td>
                        <td tabindex="-1"></td>
                    </tr>
                </tbody></table>
                """

    parser = IAMActionHTMLParser()
    parser.feed(html)
    assert parser.rows == [
        [
            "AssociateDirectory",
            "Grants permission to connect a directory to be used by AWS IAM Identity Center",
            "Write",
            "",
            "",
            "ds:AuthorizeApplication",
        ],
        [
            "AssociateProfile",
            "Grants permission to create an association between a directory user or group and a profile",
            "Write",
            "",
            "",
            "",
        ],
        [
            "AttachCustomerManagedPolicyReferenceToPermissionSet",
            "Grants permission to attach a customer managed policy reference to a permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "AttachCustomerManagedPolicyReferenceToPermissionSet",
            "Grants permission to attach a customer managed policy reference to a permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "AttachManagedPolicyToPermissionSet",
            "Grants permission to attach an AWS managed policy to a permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "AttachManagedPolicyToPermissionSet",
            "Grants permission to attach an AWS managed policy to a permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "CreateAccountAssignment",
            "Grants permission to assign access to a Principal for a specified AWS account using a specified permission set",
            "Write",
            "Account*",
            "",
            "",
        ],
        [
            "CreateAccountAssignment",
            "Grants permission to assign access to a Principal for a specified AWS account using a specified permission set",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "CreateAccountAssignment",
            "Grants permission to assign access to a Principal for a specified AWS account using a specified permission set",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "CreateApplication",
            "Grants permission to create an application",
            "Write",
            "ApplicationProvider*",
            "",
            "",
        ],
        [
            "CreateApplication",
            "Grants permission to create an application",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "CreateApplication",
            "Grants permission to create an application",
            "Write",
            "",
            "aws:RequestTag/${TagKey},aws:TagKeys",
            "",
        ],
        [
            "CreateApplicationAssignment",
            "Grants permission to create an application assignment",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "CreateApplicationAssignment",
            "Grants permission to create an application assignment",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "CreateApplicationInstance",
            "Grants permission to add an application instance to AWS IAM Identity Center",
            "Write",
            "",
            "",
            "",
        ],
        [
            "CreateApplicationInstanceCertificate",
            "Grants permission to add a new certificate for an application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "CreateInstance",
            "Grants permission to create an identity center instance",
            "Write",
            "Instance*",
            "",
            "iam:CreateServiceLinkedRole,organizations:DescribeOrganization",
        ],
        [
            "CreateInstance",
            "Grants permission to create an identity center instance",
            "Write",
            "",
            "aws:RequestTag/${TagKey},aws:TagKeys",
            "",
        ],
        [
            "CreateInstanceAccessControlAttributeConfiguration",
            "Grants permission to enable the instance for ABAC and specify the attributes",
            "Write",
            "Instance*",
            "",
            "iam:AttachRolePolicy,iam:CreateRole,iam:DeleteRole,iam:DeleteRolePolicy,iam:DetachRolePolicy,iam:GetRole,iam:ListAttachedRolePolicies,iam:ListRolePolicies,iam:PutRolePolicy,iam:UpdateAssumeRolePolicy",
        ],
        [
            "CreateManagedApplicationInstance",
            "Grants permission to add a managed application instance to AWS IAM Identity Center",
            "Write",
            "",
            "",
            "",
        ],
        [
            "CreatePermissionSet",
            "Grants permission to create a permission set",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "CreatePermissionSet",
            "Grants permission to create a permission set",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "CreatePermissionSet",
            "Grants permission to create a permission set",
            "Write",
            "",
            "aws:RequestTag/${TagKey},aws:TagKeys",
            "",
        ],
        [
            "CreateProfile",
            "Grants permission to create a profile for an application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "CreateTrust",
            "Grants permission to create a federation trust in a target account",
            "Write",
            "",
            "",
            "",
        ],
        [
            "CreateTrustedTokenIssuer",
            "Grants permission to create a trusted token issuer for an instance",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "CreateTrustedTokenIssuer",
            "Grants permission to create a trusted token issuer for an instance",
            "Write",
            "",
            "aws:RequestTag/${TagKey},aws:TagKeys",
            "",
        ],
        [
            "DeleteAccountAssignment",
            "Grants permission to delete a Principal's access from a specified AWS account using a specified permission set",
            "Write",
            "Account*",
            "",
            "",
        ],
        [
            "DeleteAccountAssignment",
            "Grants permission to delete a Principal's access from a specified AWS account using a specified permission set",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "DeleteAccountAssignment",
            "Grants permission to delete a Principal's access from a specified AWS account using a specified permission set",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DeleteApplication",
            "Grants permission to delete an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "DeleteApplication",
            "Grants permission to delete an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DeleteApplicationAccessScope",
            "Grants permission to delete an access scope to an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "DeleteApplicationAccessScope",
            "Grants permission to delete an access scope to an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DeleteApplicationAssignment",
            "Grants permission to delete an application assignment",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "DeleteApplicationAssignment",
            "Grants permission to delete an application assignment",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DeleteApplicationAuthenticationMethod",
            "Grants permission to delete an authentication method to an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "DeleteApplicationAuthenticationMethod",
            "Grants permission to delete an authentication method to an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DeleteApplicationGrant",
            "Grants permission to delete a grant from an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "DeleteApplicationGrant",
            "Grants permission to delete a grant from an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DeleteApplicationInstance",
            "Grants permission to delete the application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "DeleteApplicationInstanceCertificate",
            "Grants permission to delete an inactive or expired certificate from the application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "DeleteInlinePolicyFromPermissionSet",
            "Grants permission to delete the inline policy from a specified permission set",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "DeleteInlinePolicyFromPermissionSet",
            "Grants permission to delete the inline policy from a specified permission set",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DeleteInstance",
            "Grants permission to delete an identity center instance",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "DeleteInstanceAccessControlAttributeConfiguration",
            "Grants permission to disable ABAC and remove the attributes list for the instance",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "DeleteManagedApplicationInstance",
            "Grants permission to delete the managed application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "DeletePermissionSet",
            "Grants permission to delete a permission set",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "DeletePermissionSet",
            "Grants permission to delete a permission set",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DeletePermissionsBoundaryFromPermissionSet",
            "Grants permission to remove permissions boundary from a permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "DeletePermissionsBoundaryFromPermissionSet",
            "Grants permission to remove permissions boundary from a permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DeletePermissionsPolicy",
            "Grants permission to delete the permission policy associated with a permission set",
            "Permissions management",
            "",
            "",
            "",
        ],
        [
            "DeleteProfile",
            "Grants permission to delete the profile for an application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "DeleteTrustedTokenIssuer",
            "Grants permission to delete a trusted token issuer for an instance",
            "Write",
            "TrustedTokenIssuer*",
            "",
            "",
        ],
        [
            "DescribeAccountAssignmentCreationStatus",
            "Grants permission to describe the status of the assignment creation request",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "DescribeAccountAssignmentDeletionStatus",
            "Grants permission to describe the status of an assignment deletion request",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "DescribeApplication",
            "Grants permission to obtain information about an application",
            "Read",
            "Application*",
            "",
            "",
        ],
        [
            "DescribeApplication",
            "Grants permission to obtain information about an application",
            "Read",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DescribeApplicationAssignment",
            "Grants permission to retrieve an application assignment",
            "Read",
            "Application*",
            "",
            "",
        ],
        [
            "DescribeApplicationAssignment",
            "Grants permission to retrieve an application assignment",
            "Read",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "DescribeApplicationProvider",
            "Grants permission to describe an application provider",
            "Read",
            "ApplicationProvider*",
            "",
            "",
        ],
        [
            "DescribeDirectories",
            "Grants permission to obtain information about the directories for this account",
            "Read",
            "",
            "",
            "",
        ],
        [
            "DescribeInstance",
            "Grants permission to obtain information about an identity center instance",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "DescribeInstanceAccessControlAttributeConfiguration",
            "Grants permission to get the list of attributes used by the instance for ABAC",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "DescribePermissionSet",
            "Grants permission to describe a permission set",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "DescribePermissionSet",
            "Grants permission to describe a permission set",
            "Read",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DescribePermissionSetProvisioningStatus",
            "Grants permission to describe the status for the given Permission Set Provisioning request",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "DescribePermissionsPolicies",
            "Grants permission to retrieve all the permissions policies associated with a permission set",
            "Read",
            "",
            "",
            "",
        ],
        [
            "DescribeRegisteredRegions",
            "Grants permission to obtain the regions where your organization has enabled AWS IAM Identity Center",
            "Read",
            "",
            "",
            "",
        ],
        [
            "DescribeTrustedTokenIssuer",
            "Grants permission to describe a trusted token issuer for an instance",
            "Read",
            "TrustedTokenIssuer*",
            "",
            "",
        ],
        [
            "DescribeTrusts",
            "Grants permission to obtain information about the trust relationships for this account",
            "Read",
            "",
            "",
            "",
        ],
        [
            "DetachCustomerManagedPolicyReferenceFromPermissionSet",
            "Grants permission to detach a customer managed policy reference from a permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "DetachCustomerManagedPolicyReferenceFromPermissionSet",
            "Grants permission to detach a customer managed policy reference from a permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DetachManagedPolicyFromPermissionSet",
            "Grants permission to detach the attached AWS managed policy from the specified permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "DetachManagedPolicyFromPermissionSet",
            "Grants permission to detach the attached AWS managed policy from the specified permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "DisassociateDirectory",
            "Grants permission to disassociate a directory to be used by AWS IAM Identity Center",
            "Write",
            "",
            "",
            "ds:UnauthorizeApplication",
        ],
        [
            "DisassociateProfile",
            "Grants permission to disassociate a directory user or group from a profile",
            "Write",
            "",
            "",
            "",
        ],
        [
            "GetApplicationAccessScope",
            "Grants permission to get an access scope to an application",
            "Read",
            "Application*",
            "",
            "",
        ],
        [
            "GetApplicationAccessScope",
            "Grants permission to get an access scope to an application",
            "Read",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "GetApplicationAssignmentConfiguration",
            "Grants permission to read assignment configurations for an application",
            "Read",
            "Application*",
            "",
            "",
        ],
        [
            "GetApplicationAssignmentConfiguration",
            "Grants permission to read assignment configurations for an application",
            "Read",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "GetApplicationAuthenticationMethod",
            "Grants permission to get an authentication method to an application",
            "Read",
            "Application*",
            "",
            "",
        ],
        [
            "GetApplicationAuthenticationMethod",
            "Grants permission to get an authentication method to an application",
            "Read",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "GetApplicationGrant",
            "Grants permission to obtain details about a grant belonging to an application",
            "Read",
            "Application*",
            "",
            "",
        ],
        [
            "GetApplicationGrant",
            "Grants permission to obtain details about a grant belonging to an application",
            "Read",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "GetApplicationInstance",
            "Grants permission to retrieve details for an application instance",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetApplicationTemplate",
            "Grants permission to retrieve application template details",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetInlinePolicyForPermissionSet",
            "Grants permission to obtain the inline policy assigned to the permission set",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "GetInlinePolicyForPermissionSet",
            "Grants permission to obtain the inline policy assigned to the permission set",
            "Read",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "GetManagedApplicationInstance",
            "Grants permission to retrieve details for an application instance",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetMfaDeviceManagementForDirectory",
            "Grants permission to retrieve Mfa Device Management settings for the directory",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetPermissionSet",
            "Grants permission to retrieve details of a permission set",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetPermissionsBoundaryForPermissionSet",
            "Grants permission to get permissions boundary for a permission set",
            "Read",
            "Instance*",
            "",
            "",
        ],
        [
            "GetPermissionsBoundaryForPermissionSet",
            "Grants permission to get permissions boundary for a permission set",
            "Read",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "GetPermissionsPolicy",
            "Grants permission to retrieve all permission policies associated with a permission set",
            "Read",
            "",
            "",
            "sso:DescribePermissionsPolicies",
        ],
        [
            "GetProfile",
            "Grants permission to retrieve a profile for an application instance",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetSSOStatus",
            "Grants permission to check if AWS IAM Identity Center is enabled",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetSharedSsoConfiguration",
            "Grants permission to retrieve shared configuration for the current SSO instance",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetSsoConfiguration",
            "Grants permission to retrieve configuration for the current SSO instance",
            "Read",
            "",
            "",
            "",
        ],
        [
            "GetTrust",
            "Grants permission to retrieve the federation trust in a target account",
            "Read",
            "",
            "",
            "",
        ],
        [
            "ImportApplicationInstanceServiceProviderMetadata",
            "Grants permission to update the application instance by uploading an application SAML metadata file provided by the service provider",
            "Write",
            "",
            "",
            "",
        ],
        [
            "ListAccountAssignmentCreationStatus",
            "Grants permission to list the status of the AWS account assignment creation requests for a specified SSO instance",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListAccountAssignmentDeletionStatus",
            "Grants permission to list the status of the AWS account assignment deletion requests for a specified SSO instance",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListAccountAssignments",
            "Grants permission to list the assignee of the specified AWS account with the specified permission set",
            "List",
            "Account*",
            "",
            "",
        ],
        [
            "ListAccountAssignments",
            "Grants permission to list the assignee of the specified AWS account with the specified permission set",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListAccountAssignments",
            "Grants permission to list the assignee of the specified AWS account with the specified permission set",
            "List",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "ListAccountAssignmentsForPrincipal",
            "Grants permission to list accounts assigned to user or group",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListAccountsForProvisionedPermissionSet",
            "Grants permission to list all the AWS accounts where the specified permission set is provisioned",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListAccountsForProvisionedPermissionSet",
            "Grants permission to list all the AWS accounts where the specified permission set is provisioned",
            "List",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "ListApplicationAccessScopes",
            "Grants permission to list access scopes to an application",
            "List",
            "Application*",
            "",
            "",
        ],
        [
            "ListApplicationAccessScopes",
            "Grants permission to list access scopes to an application",
            "List",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "ListApplicationAssignments",
            "Grants permission to list application assignments",
            "List",
            "Application*",
            "",
            "",
        ],
        [
            "ListApplicationAssignments",
            "Grants permission to list application assignments",
            "List",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "ListApplicationAssignmentsForPrincipal",
            "Grants permission to list applications assigned to user or group",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListApplicationAssignmentsForPrincipal",
            "Grants permission to list applications assigned to user or group",
            "List",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "ListApplicationAuthenticationMethods",
            "Grants permission to list authentication methods to an application",
            "List",
            "Application*",
            "",
            "",
        ],
        [
            "ListApplicationAuthenticationMethods",
            "Grants permission to list authentication methods to an application",
            "List",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "ListApplicationGrants",
            "Grants permission to list grants from an application",
            "List",
            "Application*",
            "",
            "",
        ],
        [
            "ListApplicationGrants",
            "Grants permission to list grants from an application",
            "List",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "ListApplicationInstanceCertificates",
            "Grants permission to retrieve all of the certificates for a given application instance",
            "Read",
            "",
            "",
            "",
        ],
        [
            "ListApplicationInstances",
            "Grants permission to retrieve all application instances",
            "List",
            "",
            "",
            "sso:GetApplicationInstance",
        ],
        [
            "ListApplicationProviders",
            "Grants permission to list application providers",
            "List",
            "ApplicationProvider*",
            "",
            "",
        ],
        [
            "ListApplicationTemplates",
            "Grants permission to retrieve all supported application templates",
            "List",
            "",
            "",
            "sso:GetApplicationTemplate",
        ],
        [
            "ListApplications",
            "Grants permission to retrieve all applications associated with the instance of IAM Identity Center",
            "List",
            "",
            "",
            "",
        ],
        [
            "ListCustomerManagedPolicyReferencesInPermissionSet",
            "Grants permission to list the customer managed policy references that are attached to a permission set",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListCustomerManagedPolicyReferencesInPermissionSet",
            "Grants permission to list the customer managed policy references that are attached to a permission set",
            "List",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "ListDirectoryAssociations",
            "Grants permission to retrieve details about the directory connected to AWS IAM Identity Center",
            "Read",
            "",
            "",
            "",
        ],
        [
            "ListInstances",
            "Grants permission to list the SSO Instances that the caller has access to",
            "List",
            "",
            "",
            "",
        ],
        [
            "ListManagedPoliciesInPermissionSet",
            "Grants permission to list the AWS managed policies that are attached to a specified permission set",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListManagedPoliciesInPermissionSet",
            "Grants permission to list the AWS managed policies that are attached to a specified permission set",
            "List",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "ListPermissionSetProvisioningStatus",
            "Grants permission to list the status of the Permission Set Provisioning requests for a specified SSO instance",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListPermissionSets",
            "Grants permission to retrieve all permission sets",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListPermissionSetsProvisionedToAccount",
            "Grants permission to list all the permission sets that are provisioned to a specified AWS account",
            "List",
            "Account*",
            "",
            "",
        ],
        [
            "ListPermissionSetsProvisionedToAccount",
            "Grants permission to list all the permission sets that are provisioned to a specified AWS account",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ListProfileAssociations",
            "Grants permission to retrieve the directory user or group associated with the profile",
            "Read",
            "",
            "",
            "",
        ],
        [
            "ListProfiles",
            "Grants permission to retrieve all profiles for an application instance",
            "List",
            "",
            "",
            "sso:GetProfile",
        ],
        [
            "ListTagsForResource",
            "Grants permission to list the tags that are attached to a specified resource",
            "Read",
            "Application",
            "",
            "",
        ],
        [
            "ListTagsForResource",
            "Grants permission to list the tags that are attached to a specified resource",
            "Read",
            "Instance",
            "",
            "",
        ],
        [
            "ListTagsForResource",
            "Grants permission to list the tags that are attached to a specified resource",
            "Read",
            "PermissionSet",
            "",
            "",
        ],
        [
            "ListTagsForResource",
            "Grants permission to list the tags that are attached to a specified resource",
            "Read",
            "TrustedTokenIssuer",
            "",
            "",
        ],
        [
            "ListTrustedTokenIssuers",
            "Grants permission to list trusted token issuers for an instance",
            "List",
            "Instance*",
            "",
            "",
        ],
        [
            "ProvisionPermissionSet",
            "Grants permission to provision a specified permission set to the specified target",
            "Write",
            "Account*",
            "",
            "",
        ],
        [
            "ProvisionPermissionSet",
            "Grants permission to provision a specified permission set to the specified target",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "ProvisionPermissionSet",
            "Grants permission to provision a specified permission set to the specified target",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "PutApplicationAccessScope",
            "Grants permission to create/update an access scope to an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "PutApplicationAccessScope",
            "Grants permission to create/update an access scope to an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "PutApplicationAssignmentConfiguration",
            "Grants permission to add assignment configurations to an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "PutApplicationAssignmentConfiguration",
            "Grants permission to add assignment configurations to an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "PutApplicationAuthenticationMethod",
            "Grants permission to create/update an authentication method to an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "PutApplicationAuthenticationMethod",
            "Grants permission to create/update an authentication method to an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "PutApplicationGrant",
            "Grants permission to create/update a grant to an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "PutApplicationGrant",
            "Grants permission to create/update a grant to an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "PutInlinePolicyToPermissionSet",
            "Grants permission to attach an IAM inline policy to a permission set",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "PutInlinePolicyToPermissionSet",
            "Grants permission to attach an IAM inline policy to a permission set",
            "Write",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "PutMfaDeviceManagementForDirectory",
            "Grants permission to put Mfa Device Management settings for the directory",
            "Write",
            "",
            "",
            "",
        ],
        [
            "PutPermissionsBoundaryToPermissionSet",
            "Grants permission to add permissions boundary to a permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "PutPermissionsBoundaryToPermissionSet",
            "Grants permission to add permissions boundary to a permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "PutPermissionsPolicy",
            "Grants permission to add a policy to a permission set",
            "Permissions management",
            "",
            "",
            "",
        ],
        [
            "SearchGroups",
            "Grants permission to search for groups within the associated directory",
            "Read",
            "",
            "",
            "ds:DescribeDirectories",
        ],
        [
            "SearchUsers",
            "Grants permission to search for users within the associated directory",
            "Read",
            "",
            "",
            "ds:DescribeDirectories",
        ],
        [
            "StartSSO",
            "Grants permission to initialize AWS IAM Identity Center",
            "Write",
            "",
            "",
            "organizations:DescribeOrganization,organizations:EnableAWSServiceAccess",
        ],
        [
            "TagResource",
            "Grants permission to associate a set of tags with a specified resource",
            "Tagging",
            "Application",
            "",
            "",
        ],
        [
            "TagResource",
            "Grants permission to associate a set of tags with a specified resource",
            "Tagging",
            "Instance",
            "",
            "",
        ],
        [
            "TagResource",
            "Grants permission to associate a set of tags with a specified resource",
            "Tagging",
            "PermissionSet",
            "",
            "",
        ],
        [
            "TagResource",
            "Grants permission to associate a set of tags with a specified resource",
            "Tagging",
            "TrustedTokenIssuer",
            "",
            "",
        ],
        [
            "TagResource",
            "Grants permission to associate a set of tags with a specified resource",
            "Tagging",
            "",
            "aws:RequestTag/${TagKey},aws:TagKeys",
            "",
        ],
        [
            "UntagResource",
            "Grants permission to disassociate a set of tags from a specified resource",
            "Tagging",
            "Application",
            "",
            "",
        ],
        [
            "UntagResource",
            "Grants permission to disassociate a set of tags from a specified resource",
            "Tagging",
            "Instance",
            "",
            "",
        ],
        [
            "UntagResource",
            "Grants permission to disassociate a set of tags from a specified resource",
            "Tagging",
            "PermissionSet",
            "",
            "",
        ],
        [
            "UntagResource",
            "Grants permission to disassociate a set of tags from a specified resource",
            "Tagging",
            "TrustedTokenIssuer",
            "",
            "",
        ],
        [
            "UntagResource",
            "Grants permission to disassociate a set of tags from a specified resource",
            "Tagging",
            "",
            "aws:TagKeys",
            "",
        ],
        [
            "UpdateApplication",
            "Grants permission to update an application",
            "Write",
            "Application*",
            "",
            "",
        ],
        [
            "UpdateApplication",
            "Grants permission to update an application",
            "Write",
            "",
            "sso:ApplicationAccount",
            "",
        ],
        [
            "UpdateApplicationInstanceActiveCertificate",
            "Grants permission to set a certificate as the active one for this application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateApplicationInstanceDisplayData",
            "Grants permission to update display data of an application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateApplicationInstanceResponseConfiguration",
            "Grants permission to update federation response configuration for the application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateApplicationInstanceResponseSchemaConfiguration",
            "Grants permission to update federation response schema configuration for the application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateApplicationInstanceSecurityConfiguration",
            "Grants permission to update security details for the application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateApplicationInstanceServiceProviderConfiguration",
            "Grants permission to update service provider related configuration for the application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateApplicationInstanceStatus",
            "Grants permission to update the status of an application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateDirectoryAssociation",
            "Grants permission to update the user attribute mappings for your connected directory",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateInstance",
            "Grants permission to update an identity center instance",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "UpdateInstanceAccessControlAttributeConfiguration",
            "Grants permission to update the attributes to use with the instance for ABAC",
            "Write",
            "Instance*",
            "",
            "",
        ],
        [
            "UpdateManagedApplicationInstanceStatus",
            "Grants permission to update the status of a managed application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdatePermissionSet",
            "Grants permission to update the permission set",
            "Permissions management",
            "Instance*",
            "",
            "",
        ],
        [
            "UpdatePermissionSet",
            "Grants permission to update the permission set",
            "Permissions management",
            "PermissionSet*",
            "",
            "",
        ],
        [
            "UpdateProfile",
            "Grants permission to update the profile for an application instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateSSOConfiguration",
            "Grants permission to update the configuration for the current SSO instance",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateTrust",
            "Grants permission to update the federation trust in a target account",
            "Write",
            "",
            "",
            "",
        ],
        [
            "UpdateTrustedTokenIssuer",
            "Grants permission to update a trusted token issuer for an instance",
            "Write",
            "TrustedTokenIssuer*",
            "",
            "",
        ],
    ]
