from enum import Enum
from typing import Dict, List, Optional

from mypy_boto3_athena import AthenaClient
from mypy_boto3_glue import GlueClient
from mypy_boto3_s3 import S3Client, S3ServiceResource
from mypy_boto3_secretsmanager import SecretsManagerClient
from mypy_boto3_ses import SESClient
from mypy_boto3_sqs import SQSClient
from pydantic import BaseModel, EmailStr

#
# GENERIC
#


class AuthConfig(BaseModel):
    cache_update_threshold: int
    cookie_max_age_days: int
    cookie_security: bool
    cors_allow_origin: str
    honeycomb_secret_id: Optional[str]  # honeycomb.io API key
    jwt_name: str  # jwt-ci | jwt-dev | jwt-prod
    jwt_algorithm: str  # ES256
    jwt_audience: str  # DatadeftDev | DepoxyProd | HexaLoc | Etc.
    jwt_secret_id: str  # SecretsManager secret id for Signing key
    s3_bucket: str
    ses_email_subject: str
    ses_from_email: EmailStr
    stage: str
    allowed_email_domains: str  # Email domains from which a user log in, a column-separated string


class AuthClients:
    s3_client: S3Client = None
    s3_resource: S3ServiceResource = None
    sqs_client: SQSClient = None
    secretsmanager_client: SecretsManagerClient = None
    glue_client: GlueClient = None
    ses_client: SESClient = None
    athena_client: AthenaClient = None

    def __init__(
        self,
        s3_client: S3Client,
        s3_resource: S3ServiceResource,
        sqs_client: SQSClient,
        secretsmanager_client: SecretsManagerClient,
        glue_client: GlueClient,
        ses_client: SESClient,
        athena_client: AthenaClient,
    ):
        self.s3_client: S3Client = s3_client
        self.s3_resource: S3ServiceResource = s3_resource
        self.sqs_client: SQSClient = sqs_client
        self.secretsmanager_client: SecretsManagerClient = secretsmanager_client
        self.glue_client: GlueClient = glue_client
        self.ses_client: SESClient = ses_client
        self.athena_client: AthenaClient = athena_client


class CustomError(BaseModel):
    message: str
    reasons: List[str]


#
# HTTP
#


class HttpSuccess(BaseModel):
    ok: str


class HttpError(BaseModel):
    status_code: int
    error: CustomError


#
# LOGIN - JWT
#


class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"


class JwtParam(BaseModel):
    email: EmailStr
    first_name: str
    role: RoleEnum


class JwtParamHexa(BaseModel):
    email: EmailStr
    first_name: str
    role: RoleEnum
    org_id: str
    user_id: str


class MagicLinkDto(BaseModel):
    email: str
    firstName: str
    acceptedTermsAndConditions: bool
    acceptedGdprTerms: bool
    acceptedCookiePolicy: bool
    now: str


class MagicLinkDomain(BaseModel):
    email: EmailStr
    first_name: str
    accepted_terms_and_conditions: bool
    accepted_gdpr_terms: bool
    accepted_cookie_policy: bool
    now: str


class MagicLinkInternal(BaseModel):
    magic_link: MagicLinkDomain
    hash: str
    source_ip: str


class LoginHash(BaseModel):
    hash: str


class WhoAmI(BaseModel):
    email: EmailStr
    firstName: str
    role: RoleEnum


class WhoAmIHexa(BaseModel):
    email: EmailStr
    firstName: str
    role: RoleEnum
    orgId: str
    userId: str


class UserEmailAndId(BaseModel):
    emailAddress: EmailStr
    userId: str


class EmailDomainAndOrgId(BaseModel):
    emailDomain: str
    orgId: str


#
# FEATURE REQUEST
#


class StatusEnum(str, Enum):
    created = "created"
    accepted = "accepted"
    wip = "wip"
    implemented = "implemented"
    rejected = "rejected"


class TypeEnum(str, Enum):
    feature = "feature"
    bug = "bug"


class FeatureRequest(BaseModel):
    uuid: Optional[str]
    title: str
    type: TypeEnum
    description: str
    author: EmailStr
    status: StatusEnum


class FeatureRequestList(BaseModel):
    __root__: List[FeatureRequest]


class FeatureRequestMeta(BaseModel):
    uuid: str
    upvoteCount: int
    currentUserVoted: bool


class FeatureRequestMetaList(BaseModel):
    __root__: List[FeatureRequestMeta]


########### DEPOXY


class Database(BaseModel):
    databaseEid: str
    databaseName: str
    description: str
    createTime: str
    catalogId: str

    # @validator('createTime')
    # def create_time_iso_8601(cls, v: str):
    #    ...


class Databases(BaseModel):
    __root__: List[Database]


class Column(BaseModel):
    name: str
    type: str
    comment: str


class SerdeInfo(BaseModel):
    serializationLibrary: str
    parameters: Dict


class StorageDescriptor(BaseModel):
    location: str
    inputFormat: str
    outputFormat: str
    isCompressed: bool
    numberOfBuckets: int
    bucketColumns: List
    sortColumns: List
    parameters: Dict
    isStoredAsSubDirectories: bool


class PartitionKey(BaseModel):
    name: str
    type: str
    comment: str


class GeneralInfo(BaseModel):
    tableEid: str
    tableName: str
    databaseName: str
    createTime: str  # TODO: validator
    updateTime: str  # TODO: validator
    tableType: str
    createdBy: str
    versionId: str
    catalogId: str
    isRegisteredWithLakeFormation: bool


class TableDetail(BaseModel):
    generalInfo: GeneralInfo
    storageDescriptor: StorageDescriptor
    serdeInfo: SerdeInfo
    partitionKeys: List[PartitionKey]
    columns: List[Column]


class TableDetails(BaseModel):
    __root__: List[TableDetail]


class TableSummary(BaseModel):
    table_eid: str
    table_name: str
    database_eid: str
    database_name: str
    create_time: str  # TODO: validator
    update_time: str  # TODO: validator
    location: str


class TableSummaries(BaseModel):
    __root__: List[TableSummary]


class TableSummaryDto(BaseModel):
    tableEid: str
    tableName: str
    databaseEid: str
    databaseName: str
    createTime: str  # TODO: validator
    updateTime: str  # TODO: validator
    location: str


class TableSummariesDto(BaseModel):
    __root__: List[TableSummaryDto]


#######################


class QuerySummary(BaseModel):
    query_execution_id: str
    query_state: str
    query_start: str  # TODO: validator
    query_run_time_ms: int
    query_data_scanned_in_mib: float


class QuerySummaries(BaseModel):
    __root__: List[QuerySummary]


class QuerySummaryDto(BaseModel):
    queryExecutionId: str
    queryState: str
    queryStart: str  # TODO: validator
    queryRunTimeMs: int
    queryDataScannedInMib: float


class QuerySummariesDto(BaseModel):
    __root__: List[QuerySummaryDto]


class Statistics(BaseModel):
    engineExecutionTime: int
    dataScannedInMiB: float
    totalExecutionTime: int
    queryQueueTime: int
    queryPlanningTime: Optional[int]
    serviceProcessingTime: int


class QueryDetail(BaseModel):
    queryExecutionId: str
    query: str
    statementType: str
    outputLocation: Optional[str]
    encryptionOption: Optional[str]
    kmsKey: Optional[str]
    database: str
    catalog: str
    status: str
    submissionDate: str  # TODO: validator
    completionDate: Optional[str]  # TODO: validator
    errorMessage: Optional[str]
    workGroup: str
    statistics: Statistics


#############################


class JobSummary(BaseModel):
    job_eid: str
    job_name: str
    last_job_run_state: Optional[str]
    last_started_on: Optional[str]
    last_completed_on: Optional[str]
    last_execution_time: Optional[int]


class JobSummaryDto(BaseModel):
    jobEid: str
    jobName: str
    lastJobRunState: Optional[str]
    lastStartedOn: Optional[str]
    lastCompletedOn: Optional[str]
    lastExecutionTime: Optional[int]


class JobSummaries(BaseModel):
    __root__: List[JobSummary]


class JobSummariesDto(BaseModel):
    __root__: List[JobSummaryDto]


class Command(BaseModel):
    name: str
    scriptLocation: str
    pythonVersion: str


class JobDetail(BaseModel):
    jobEid: str
    jobName: str
    description: str
    role: str
    createdOn: str
    lastModifiedOn: str
    glueVersion: str
    maxRetries: int
    allocatedCapacity: int
    maxCapacity: int
    timeout: int
    workerType: Optional[str]
    numberOfWorkers: Optional[int]
    command: Optional[Command]
    defaultArguments: Optional[Dict]
    lastJobRunState: Optional[str]
    lastStartedOn: Optional[str]
    lastCompletedOn: Optional[str]
    lastExecutionTime: Optional[int]


class JobRun(BaseModel):
    jobRunAwsId: str
    jobName: str
    jobEid: str
    triggerName: Optional[str]
    jobRunState: str
    startedOn: str  # TODO: validator
    completedOn: str  # TODO: validator
    executionTime: int
    errorMessage: Optional[str]


class JobRuns(BaseModel):
    __root__: List[JobRun]


class JobTrigger(BaseModel):
    triggerName: str
    triggerType: str
    triggerState: str
    triggerSchedule: str


class JobTriggers(BaseModel):
    __root__: List[JobTrigger]


##########################


class TableMeta(BaseModel):
    databaseName: str
    tableName: str
    sizeIecMiB: float
    fileCount: int


class TableMetaList(BaseModel):
    __root__: List[TableMeta]


class TableTreemap(BaseModel):
    tableName: str
    sizeIecMiB: float
    fileCount: int


class DatabaseTreemap(BaseModel):
    databaseName: str
    tables: List[TableTreemap]


class TablesTreemap(BaseModel):
    __root__: List[DatabaseTreemap]


################ dashboard - top queries


class QueryExecutionSummary(BaseModel):
    queryExecutionId: str
    runTimeSeconds: float
    dataScannedIecMiB: float


class TopQueries(BaseModel):
    total: float
    topQueries: List[QueryExecutionSummary]


################ dashboard - top failed jobs


class JobRunSummary(BaseModel):
    jobName: str
    jobEid: str
    numOfFailes: str


class TopFailedJobs(BaseModel):
    total: float
    topJobs: List[JobRunSummary]


################ cache


class EidCache(BaseModel):
    forward_dict: Dict[str, str]
    reverse_dict: Dict[str, str]
    created_at: Optional[str]
    request_count: int = 0


class JobSummariesCache(BaseModel):
    job_summaries: JobSummaries
    created_at: Optional[str]
    request_count: int = 0


class TableSummariesCache(BaseModel):
    table_summaries: TableSummaries
    created_at: Optional[str]
    request_count: int = 0


class QuerySummariesCache(BaseModel):
    query_summaries: QuerySummaries
    created_at: Optional[str]
    request_count: int = 0


######## HEXA


class CategorySummary(BaseModel):
    categoryId: str
    categoryName: str
    description: str
    hasUnfilled: Optional[bool]


class MatGroupSummary(BaseModel):
    matGroupId: str
    matGroupName: str
    description: str
    hasUnfilled: Optional[bool]


class CategorySummaries(BaseModel):
    __root__: List[CategorySummary]


class MatGroupSummaries(BaseModel):
    __root__: List[MatGroupSummary]


class EvaluationSummary(BaseModel):
    evaluationId: str
    evaluationName: str
    matId: str
    status: str
    createDate: str
    dueDate: str
    fillDate: Optional[str]
    targetGroup: str


class EvaluationSummaries(BaseModel):
    __root__: List[Optional[EvaluationSummary]]


class Question(BaseModel):
    label: Optional[str]
    d1: str
    d2: str
    d3: str


class Questions(BaseModel):
    q1: Question
    q2: Question
    q3: Question
    q4: Question
    q5: Question


class EmptyEvaluation(BaseModel):
    evaluationId: str
    evaluationName: str
    matId: str
    matGroupId: str
    questions: Optional[Questions]


class HexaIdEnum(str, Enum):
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
    h7 = "h7"
    h8 = "h8"
    h9 = "h9"
    h10 = "h10"
    h11 = "h11"


class HexaSideEnum(str, Enum):
    s1 = "s1"
    s2 = "s2"
    s3 = "s3"


class Answer(BaseModel):
    hexaId: HexaIdEnum
    d1: HexaSideEnum
    d2: HexaSideEnum
    d3: HexaSideEnum


class Answers(BaseModel):
    a1: Answer
    a2: Answer
    a3: Answer
    a4: Answer
    a5: Answer


class MatLayoutEnum(str, Enum):
    A = "A"
    B = "B"


class Mat(BaseModel):
    matId: str
    matName: str
    matLayout: MatLayoutEnum
    description: str
    createDate: str
    dueDate: str
    targetGroup: str
    questions: Questions


class MatSummary(BaseModel):
    matId: str
    matName: str
    createDate: str
    dueDate: str
    targetGroup: str
    targetCount: int
    fillCount: int


class FilledEvaluation(BaseModel):
    evaluationId: str
    evaluationName: str
    matId: str
    matGroupId: str
    questions: Optional[Questions]
    answers: Answers


class FilledEvaluations(BaseModel):
    __root__: List[FilledEvaluation]


class Hexagon(BaseModel):
    hexaId: HexaIdEnum
    s1: int
    s2: int
    s3: int


class SingleReportData(BaseModel):
    name: str
    valueSum: int


class SingleReport(BaseModel):
    matId: str
    matName: str
    matGroupId: str
    matGroupName: str
    createDate: str
    dueDate: str
    targetGroup: str
    targetCount: str
    fillCount: str
    data: List[SingleReportData]


class ReportSummary(BaseModel):
    matGroupId: str
    matGroupName: str
    description: str
    mats: List[MatSummary]


class MatIds(BaseModel):
    __root__: List[str]
