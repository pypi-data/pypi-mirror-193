from dataclasses import dataclass
from typing import Dict, List

from aws_ptrp.iam.policy import PolicyDocumentCtx, UserPolicy
from aws_ptrp.principals import Principal
from aws_ptrp.ptrp_allowed_lines.allowed_line_nodes_base import PrincipalAndPoliciesNodeBase
from aws_ptrp.utils.pagination import paginate_response_list
from boto3 import Session
from serde import field, from_dict, serde


@serde
@dataclass
class IAMUser(PrincipalAndPoliciesNodeBase):
    user_name: str
    user_id: str
    path: str
    user_policies: List[UserPolicy]
    attached_policies_arn: List[str]
    identity_principal: Principal = field(
        deserializer=Principal.from_policy_principal_str,
        serializer=Principal.to_policy_principal_str,
    )

    def __eq__(self, other):
        return self.user_id == other.user_id

    def __repr__(self):
        return self.identity_principal.get_arn()

    def __hash__(self):
        return hash(self.user_id)

    @staticmethod
    def _extract_aws_account_id_from_arn_of_iam_entity(arn: str) -> str:
        return arn[arn.find(":iam::") + 6 : arn.find(":user/")]

    # # impl PrincipalAndPoliciesNodeBase
    # def get_permission_boundary(self) -> Optional[PolicyDocument]:
    #     return None

    # def get_session_policies(self) -> List[PolicyDocument]:
    #     return []

    # NodeBase
    def get_node_arn(self) -> str:
        return self.identity_principal.get_arn()

    def get_node_name(self) -> str:
        return self.identity_principal.get_name()

    # impl PrincipalNodeBase
    def get_stmt_principal(self) -> Principal:
        return self.identity_principal

    # PoliciesNodeBase
    def get_attached_policies_arn(self) -> List[str]:
        return self.attached_policies_arn

    def get_inline_policies_ctx(self) -> List[PolicyDocumentCtx]:
        arn = self.identity_principal.get_arn()
        aws_account_id = IAMUser._extract_aws_account_id_from_arn_of_iam_entity(arn)
        return list(
            map(
                lambda x: PolicyDocumentCtx(
                    policy_document=x.policy_document,
                    parent_arn=arn,
                    policy_name=x.policy_name,
                    parent_aws_account_id=aws_account_id,
                ),
                self.user_policies,
            )
        )


def get_iam_users(session: Session) -> Dict[str, IAMUser]:
    iam_client = session.client('iam')
    ret: Dict[str, IAMUser] = {}

    users = paginate_response_list(iam_client.list_users, 'Users')
    for user in users:
        user_name = user['UserName']
        user_id = user['UserId']
        arn = user['Arn']
        path = user['Path']

        user_policies_response = paginate_response_list(
            iam_client.list_user_policies, 'PolicyNames', UserName=user_name
        )
        user_policies: List[UserPolicy] = []
        for user_policy_response in user_policies_response:
            user_policies.append(
                from_dict(UserPolicy, iam_client.get_user_policy(UserName=user_name, PolicyName=user_policy_response))  # type: ignore
            )

        attached_policies = paginate_response_list(
            iam_client.list_attached_user_policies, 'AttachedPolicies', UserName=user_name
        )
        attached_policies_arn = [attached_policy['PolicyArn'] for attached_policy in attached_policies]
        user_principal_arn = Principal.load_from_iam_user(arn)
        ret[arn] = IAMUser(
            user_name=user_name,
            user_id=user_id,
            identity_principal=user_principal_arn,
            path=path,
            user_policies=user_policies,
            attached_policies_arn=attached_policies_arn,
        )

    return ret
