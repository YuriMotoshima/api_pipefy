query = {"Query":{
  "allCards": {"Describle":"CardConnection	Fetches all pipe cards based on arguments", "query":""},
  "autoFillFields": {"Describle":"[AutoFillFieldUnion]	Lookup the values that will automatically fill the child-card's start form fields", "query":""},
  "card": {"Describle":"Card	Lookup a card by its ID", "query":""},
  "cards": {"Describle":"CardConnection	Fetches a group of cards based on arguments", "query":""},
  "cardsImportations": {"Describle":"[CardsImportation]	Lookup the cards importer history by the pipe ID", "query":""},
  "conditionalField": {"Describle":"ConditionalField	", "query":""},
  "connectedTableRecords": {"Describle":"PublicTableRecordConnection	", "query":""},
  "fieldCondition": {"Describle":"FieldCondition	", "query":""},
  "findCards": {"Describle":"CardConnection	Fetch cards based on fields' inputs", "query":""},
  "findRecords": {"Describle":"CardConnection	Fetch records based on fields' inputs", "query":""},
  "inbox_emails": {"Describle":"[InboxEmail]	Lookup the card's emails by its ID", "query":""},
  "me": {"Describle":"User	Returns informations of the current authenticated user", "query":""},
  "organization": {"Describle":"Organization	Lookup an organization by its ID", "query":""},
  "organizations": {"Describle":"[Organization]	Lookup organizations by their ID", "query":""},
  "phase": {"Describle":"Phase	Lookup a phase by its ID", "query":""},
  "pipe": {"Describle":"Pipe	Lookup a pipe by its ID", "query":""},
  "pipe_relations": {"Describle":"[PipeRelation]	Lookup pipe relations by their ID", "query":""},
  "pipe_templates": {"Describle":"[PipeTemplate]	Lookup all pipe templates available on Pipefy", "query":""},
  "pipes": {"Describle":"[Pipe]	Lookup pipes by their ID", "query":""},
  "recordsImportations": {"Describle":"[RecordsImportation]	Lookup the records importer history by the table ID", "query":""},
  "repoItemForm": {"Describle":"RepoItemFormUnion	", "query":""},
  "table": {"Describle":"Table	Lookup a database table by its ID", "query":""},
  "table_record": {"Describle":"TableRecord	Lookup a record by its ID", "query":""},
  "table_records": {"Describle":"TableRecordWithCountConnection	Fetches a group of records based on arguments", "query":""},
  "table_relations": {"Describle":"[TableRelation]	Lookup table relations by their ID", "query":""},
  "tables": {"Describle":"[Table]	Lookup database tables by their ID", "query":""},
  }
}

mutation = {"Mutation":"""
cardsImporter: CardsImporterPayload	Create new cards from a xlsx file
clonePipes: ClonePipesPayload	Clones a pipe
createCard: CreateCardPayload	Creates a card
createCardRelation: CreateCardRelationPayload	Creates a card relation
createComment: CreateCommentPayload	Creates a comment
createInboxEmail: CreateInboxEmailPayload	Creates an email
createLabel: CreateLabelPayload	Creates a label
createOrganization: CreateOrganizationPayload	Creates an organization
createOrganizationWebhook: CreateOrganizationWebhookPayload	Creates a organization webhook
createPhase: CreatePhasePayload	Creates a phase
createPhaseField: CreatePhaseFieldPayload	Creates a phase field
createPipe: CreatePipePayload	Creates a pipe
createPipeRelation: CreatePipeRelationPayload	Creates a pipe relation
createPresignedUrl: CreatePresignedUrlPayload	Returns a temporary S3 presigned url to upload a file
createPresignedUrlForPipePdfTemplate: CreatePresignedUrlForPipePdfTemplatePayload	Returns a temporary S3 presigned url to upload a pdf template image
createTable: CreateTablePayload	Creates a table
createTableField: CreateTableFieldPayload	Creates a table field
createTableRecord: CreateTableRecordPayload	Creates a record
createTableRecordInRestrictedTable: CreateTableRecordInRestrictedTablePayload	Creates a record in a private table
createWebhook: CreateWebhookPayload	Creates a webhook
deleteCard: DeleteCardPayload	Deletes a card
deleteComment: DeleteCommentPayload	Deletes a comment
deleteInboxEmail: DeleteInboxEmailPayload	Deletes an email
deleteLabel: DeleteLabelPayload	Deletes a label
deleteOrganization: DeleteOrganizationPayload	Deletes an organization
deleteOrganizationWebhook: DeleteOrganizationWebhookGQLMutationPayload	Deletes a webhook
deletePhase: DeletePhasePayload	Deletes a phase
deletePhaseField: DeletePhaseFieldPayload	Deletes a phase field
deletePipe: DeletePipePayload	Deletes a pipe
deletePipeRelation: DeletePipeRelationPayload	Deletes a pipe relation
deleteTable: DeleteTablePayload	Deletes a table
deleteTableField: DeleteTableFieldPayload	Deletes a table field
deleteTableRecord: DeleteTableRecordPayload	Deletes a record
deleteWebhook: DeleteWebhookPayload	Deletes a webhook
inviteMembers: InviteMembersPayload	Invites new members for the organization
moveCardToPhase: MoveCardToPhasePayload	Moves a card to another phase
recordsImporter: RecordsImporterPayload	Create new records from a xlsx file
removeUserFromOrg: RemoveUserFromOrgPayload	Remove a user from an organization
removeUserFromPipe: RemoveUserFromPipePayload	Removes a user from pipe
removeUserFromTable: RemoveUserFromTablePayload	Removes an user from table
sendInboxEmail: SendInboxEmailPayload	Sends an email
setRole: SetRolePayload	Sets the role of a user
setRoles: SetRolesPayload	Sets role of multiple users
setSummaryAttributes: SetSummaryAttributesPayload	Sets summary attributes
setTableFieldOrder: SetTableFieldOrderPayload	Sets table field order
setTableRecordFieldValue: SetTableRecordFieldValuePayload	Sets record field value
updateCard: UpdateCardPayload	Updates an existing card
updateCardField: UpdateCardFieldPayload	Updates an existing card field
updateComment: UpdateCommentPayload	Updates an existing comment
updateFieldsValues: UpdateFieldsValuesPayload	Update one or many values of fields inside a Card or Table record.
updateLabel: UpdateLabelPayload	Updates an existing label
updateOrganization: UpdateOrganizationPayload	Updates an existing organization
updateOrganizationWebhook: UpdateOrganizationWebhookPayload	Updates an existing organization level webhook
updatePhase: UpdatePhasePayload	Updates an existing phase
updatePhaseField: UpdatePhaseFieldPayload	Updates an existing phase field
updatePipe: UpdatePipePayload	Updates an existing pipe
updatePipeRelation: UpdatePipeRelationPayload	Updates an existing pipe relation
updateTable: UpdateTablePayload	Updates an existing table
updateTableField: UpdateTableFieldPayload	Updates an existing table field
updateTableRecord: UpdateTableRecordPayload	Updates an existing record
updateWebhook: UpdateWebhookPayload	Updates an existing webhook
"""}


pipes = '''
    pipes(ids
        anyone_can_create_card
        cards_count 
        clone_from_id 
        color 
        conditionExpressionsFieldIds 
        create_card_label 
        created_at 
        description 
        expiration_time_by_unit 
        emailAddress 
        expiration_unit 
        id 
        icon 
        last_updated_by_card 
        name 
        noun 
        only_assignees_can_edit_cards 
        only_admin_can_remove_cards 
        opened_cards_count 
        organizationId 
        public 
        public_form_active 
        public_form 
        role 
        startFormPhaseId 
        suid 
        users_count 
        uuid 
        }'''

childrenRelations ='''
    childrenRelations(only_tables
      ownFieldMaps
      allChildrenMustBeDoneToFinishParent
      allChildrenMustBeDoneToMoveParent
      autoFillFieldEnabled
      canConnectExistingItems
      canConnectMultipleItems
      canCreateNewItems
      childMustExistToFinishParent
      childMustExistToMoveParent
      id
      name
      parent
    }'''
    
assignees = """
avatarUrl: String	The user avatar URL
confirmationTokenHasExpired: Boolean	Whether the user confirmation token expired and is no longer valid
confirmed: Boolean	Whether the user is confirmed or not
createdAt: String	When the user was created
departmentKey: String	The user department key
displayName: String	The user display name
email: String	The user email
hasUnreadNotifications: Boolean	Returns if the user has unread notifications
id: ID	The user ID
intercomHash: String	Return the hash reference for intercom
intercomId: ID	The user intercom reference
invited: Boolean	Whether the user was invited to register or not
locale: String	The user language
name: String	The user name
phone: String	The user's phone
preferences: UserPreference	The user preferences
signupData: String	The user template category key
timezone: String	The user time zone
username: String	The user username
uuid: ID
"""

user = """
avatarUrl: String	The user avatar URL
confirmationTokenHasExpired: Boolean	Whether the user confirmation token expired and is no longer valid
confirmed: Boolean	Whether the user is confirmed or not
createdAt: String	When the user was created
departmentKey: String	The user department key
displayName: String	The user display name
email: String	The user email
hasUnreadNotifications: Boolean	Returns if the user has unread notifications
id: ID	The user ID
intercomHash: String	Return the hash reference for intercom
intercomId: ID	The user intercom reference
invited: Boolean	Whether the user was invited to register or not
locale: String	The user language
name: String	The user name
phone: String	The user's phone
preferences: UserPreference	The user preferences
signupData: String	The user template category key
timezone: String	The user time zone
username: String	The user username
uuid: ID	The user UUID
"""

phase = """
cards: CardConnection	Fetches a group of cards based on arguments
cards_can_be_moved_to_phases: [Phase]	Information about the phases that the cards can be moved to
cards_count: Int	The phase total cards
color: String	Color of phase
created_at: DateTime	When the phase was created
description: String	The phase description
done: Boolean	Whether it is a final phase
expiredCardsCount: Int	The phase total expired cards
fieldConditions: [FieldCondition]	Information about the phase field conditions
fields: [PhaseField]	Information about the fields
id: ID	The phase ID
index: Float	The phase positional index
isDraft: Boolean	Is this phase draft?
lateCardsCount: Int	The phase total late cards
name: String	The phase name
sequentialId: String	The sequential 
"""

inbox_email = """
attachments: [EmailAttachment]	Lookup the email's attachments by its identifier.
bcc: [String]	Represents Inbox Email 'BCC' email addresses.
body: String	Represents Inbox Email body, with any eventual previous replies removed.
card: Card	Lookup the card, from which the Inbox Email was sent, by its identifier.
cc: [String]	Represents Inbox Email 'CC' email addresses.
clean_html: String	Represents Inbox Email's clean HTML, only filtering the invalid or malicious characters and tags.
clean_text: String	Represents Inbox Email's clean text, only filtering the invalid or malicious characters and tags.
from: String	Represents Inbox Email sender email address.
fromName: String	Represents Inbox Email sender's name.
id: ID	Represents each email's identifier.
main_to: String	Represents Inbox Email's primary email addresses destination.
message_id: String	Represents the Inbox Email answer message identifier.
pipe: Pipe	Lookup the pipe, from which the Inbox Email was sent, by its identifier.
raw_headers: String	Represents Inbox Email raw headers.
raw_html: String	Represents Inbox Email raw HTML format, only filtering invalid characters.
sent_via_automation: Boolean	Indicates if this email was sent using an automation
state: String	Represents Inbox Email state, which can be: * 0 - Pending * 1 - Processing * 2 - Processed * 3 - Failed
subject: String	Represents Inbox Email subject.
to: [String]	Represents Inbox Email receiver email address.
updated_at: DateTime	Represents last Inbox Email update date and time.
user: User	Lookup the email's creator.
"""

label = """
color: String	Represents the color used in the label using a hexadecimal string.
id: ID	Represents the label identifier.
name: String
"""

phase_detail = """
became_late: Boolean	Whether or not the card ever became late on a phase.
created_at: DateTime	Represents the date and time of when the card first entered the phase.
draft: Boolean	Whether or not the phase detail is in the start form.
duration: Int	Represents the seconds card stayed in the phase.
firstTimeIn: DateTime	Represents the date and time of when card first entered the phase.
lastTimeIn: DateTime	Represents the date and time of when card last entered the phase.
lastTimeOut: DateTime	Represents the date and time of when card left the phase.
phase: Phase
"""

pipe = """
anyone_can_create_card: Boolean	Whether anyone can create cards in the pipe
cards_count: Int	The pipe total cards
childrenRelations: [PipeRelation]	Information about the pipe child connections
clone_from_id: Int	Id which the Pipe was cloned from
color: String	Color of pipe/database
conditionExpressionsFieldIds: [Int]	IDs of all fields in a pipe that trigger conditionals
create_card_label: String	The content displayed in the start form button
created_at: DateTime	When the pipe was created
description: String	The Repo description
emailAddress: String	The pipe's email inbox address
expiration_time_by_unit: Int	The number used in the pipe SLA
expiration_unit: Int	The seconds of the unit used in the pipe SLA
fieldConditions: [FieldCondition]	Information about the fields conditions
icon: String	The Repo icon
id: ID	The pipe ID
improvementSetting: ImprovementSetting	Information about the pipe improvement setting
labels: [Label]	Information about the Repo labels
last_updated_by_card: DateTime	When a card was last updated in the pipe
members: [Member]	Information about the Repo members
name: String	The Repo name
noun: String	The Repo noun for their registries
only_admin_can_remove_cards: Boolean	Whether only Admins can delete cards
only_assignees_can_edit_cards: Boolean	Whether only the card assignees can edit it
opened_cards_count: Int	The total amount of cards not done
organization: Organization	Information about the organization
organizationId: ID	Card organization id
parentsRelations: [PipeRelation]	Information about the pipe parent connections
permissions: RepoPermissionsInternalGQLType	User permissions for this repo
phases: [Phase]	Information about the pipe phases
preferences: RepoPreference	Information about the pipe preferences
public: Boolean	Whether the Repo is public
publicForm: PublicFormInternal	Information about the public form settings
role: String	The current user role in the pipe
startFormFieldConditions: [FieldCondition]	Information about the start form fields conditions
startFormPhaseId: ID	The repo start form phase id
start_form_fields: [PhaseField]	Information about the start form fields
subtitleFields: PhaseFieldConnection	Fields used that is set as subtitle
suid: String	The pipe Small Unique ID
summary_attributes: [SummaryAttribute]	Information about the data selected to be shown in the summarized view
summary_options: [SummaryGroup]	Information about the Repo summary options
title_field: PhaseField	Information about the field selected to be the card title
users: [User]	Information about the pipe users
users_count: Int	The total users in the pipe
uuid: String	Unique identifier id
webhooks: [Webhook]
"""

summary = """
title: String	Represents the title of the selected field to be represented in the summary.
type: String	Field type
value: String
"""

# -------------------------------------------------

app_attachment = """
card_id: ID	
id: ID	
name: String	
suid: String	
url: String
"""

app_attachment_edge = """
cursor: String	A cursor for use in pagination.
node: AppAttachment	The item at the end of the edge.
"""

assignee_field = """
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: [PublicUser]	Assignee field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""
    
attachment = """
createdAt: Date	
createdBy: User	
field: MinimalField	
path: String	
phase: Phase	
url: String
"""

attachment_field = """
customValidation: String	The attachment field custom validation
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""

auto_fill_field_collection = """
fieldId: ID	
value: [ID]
"""

auto_fill_field_string = """
fieldId: ID	
value: String
"""

billing = """
billingNoticePeriod: Boolean	
pastDueNoticeAlert: Boolean	
upgradeOnlyFreePlan: Boolean	
"""

card = """
age: Int	The seconds since the card was created
assignees: [User]	Information about the assigned users
attachments: [Attachment]	Information about the attached files
attachments_count: Int	The card total attachments
cardAssignees: [CardAssignee]	Information about the card's assignees
checklist_items_checked_count: Int	The card total checked items
checklist_items_count: Int	The card total checklist items
child_relations: [CardRelationship]	Information about the child pipe connections
comments: [Comment]	Information about the card comments
comments_count: Int	The card total comments
createdAt: DateTime	When the card was created
createdBy: User	Information about the card creator
creatorEmail: String	The email the card creator
currentLateness: cardLateness	Information about the card lateness
current_phase: Phase	Information about the card current phase
current_phase_age: Int	The seconds since the card entered current phase
done: Boolean	Whether the card is done
due_date: DateTime	The card due date
emailMessagingAddress: String	The card email address
expiration: CardExpiration	Information about the card expiration
expired: Boolean	Whether the card is expired
fields: [CardField]	Information about the card fields
finished_at: DateTime	When the card was finished
id: ID	The card ID
inboxEmailsRead: Boolean	Information about any inbox email read status
inbox_emails: [InboxEmail]	Information about the card emails
labels: [Label]	Information about the card labels
late: Boolean	Whether the card is late
parent_relations: [CardRelationship]	Information about the parent pipe connections
path: String	The card path
phases_history: [PhaseDetail]	Information about the phases the card went through
pipe: Pipe	Information about the pipe
started_current_phase_at: DateTime	When the card first entered the current phase
subtitles: [CardField]	Information about the card subtitles
suid: String	The card Small Unique ID
summary: [Summary]	Information about the card summary layout
summary_attributes: [Summary]	Information about the card attributes summary layout
summary_fields: [Summary]	Information about the card custom fields summary layout
title: String	The card title
updated_at: DateTime	When the card was last updated
url: String	The card URL
uuid: String
"""

card_assignee = """
assignedAt: DateTime	
id: Int
"""

card_edge = """
cursor: String	A cursor for use in pagination.
node: Card	The item at the end of the edge.
"""

card_expiration = """
expiredAt: DateTime	Date and time when card has expired
shouldExpireAt: DateTime	Date and time when card should become expired
"""

card_field = """
array_value: [String]	The value of an Attachment, Checklists, Connection or Label field, processed as an array type
assignee_values: [User]	Information about the users assigned to the card
connectedRepoItems: [PublicRepoItemTypes]	Information about cards and records connected with the card
date_value: Date	The value of a Date, DateTime or DueDate field, processed as a date type
datetime_value: DateTime	The value of a DateTime or DueDate field, processed as a date and time type
field: MinimalField	Information about the card field
filled_at: DateTime	When the field was filled
float_value: Float	The field float value
indexName: String	The searcheable name
label_values: [FieldLabel]	Information about the card label
name: String	The field name
phase_field: PhaseField	Information about the field's phase
report_value: String	The field value prepared for report
updated_at: DateTime	When the field was last updated
value: String	The field value
"""

card_form = """
createButtonLabel: String	The creation button label
formFields: [RepoItemFieldsTypes]	The available fields in Pipefy
icon: String	The Repo icon
id: ID	
name: String	The Repo name
uuid: ID	The Repo UUID
"""

card_lateness = """
becameLateAt: DateTime	
id: ID	
shouldBecomeLateAt: DateTime	
sla: Int
"""

card_relation = """
childId: ID	Represents the child card identifier.
id: ID	Represents the card relation identifier.
parentId: ID	Represents the parent card identifier.
sourceId: ID	Represents the source identifier.
sourceType: String	Represents if the connection is through a PipeRelation or a Connection Field. The possible values are: - PipeRelation - Field
"""

card_relationship = """
cards: [Card]	Lookup the connected cards by their identifier.
id: ID	The relation ID
name: String	Represents the chosen name of the relation.
pipe: Pipe	Lookup the connected pipe by its identifier.
repo: RepoTypes	Lookup the connected Pipe or Table.
source_type: String
"""

cards_importation = """
createdAt: DateTime	The importation date of creation
createdBy: User	The importation creator
dateFormatted: String	The importation date of creation formatted
id: ID	The importation ID
importedCards: Int	The amount of cards imported
status: String	The importation status
url: String	The xlsx file URL
"""

checklist_horizontal_field = """
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: [String]	Horizontal checklist field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
options: [String]	The horizontal checklist options
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""

checklist_vertical_field = """
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: [String]	Vertical checklist field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
options: [String]	The vertical checklist options
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""
cnpj_field = """
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	CNPJ field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""

comment = """
author: User	Lookup the comment's creator by its identifier.
author_name: String	Represents the comment's creator name.
created_at: DateTime	Represents the comment's creation date and time.
id: ID	Represents the comment's identifier.
text: String
"""
condition = """
expressions: [ConditionExpression]	The parameters used in the condition.
expressions_structure: [[ID]]	The condition expressions order, defining groups of "AND" and "OR".
id: ID	translation missing: en.api.documentation.condition.fields.id
related_cards: [Card]
"""

conditional_field = """
fieldsToHide: [PhaseField]
"""
condition_expression="""
field_address: String	The field ID used in the condition.
id: ID	The condition ID.
operation: String	The condition operation. Valid options: - equals - not_equals - present - blank - string_contains - string_not_contains - number_greater_than - number_less_than - date_is_today - date_is_yesterday - date_in_current_week - date_in_last_week - date_in_current_month - date_in_last_month - date_in_current_year - date_in_last_year - date_is - date_is_after - date_is_before
structure_id: ID	The number used to arrange condition's expressions in groups of "AND" and "OR".
value: String
"""
connected_table="""
anyone_can_create_card: Boolean	Allows anyone to create cards
authorization: TableAuthorization	Information about the database table authorization
color: String	Color of pipe/database
conditionExpressionsFieldIds: [Int]	IDs of all fields in a pipe that trigger conditionals
create_record_button_label: String	The content displayed in the start form button
description: String	The Repo description
icon: String	The Repo icon
id: ID	The database table ID
labels: [Label]	Information about the Repo labels
members: [Member]	Information about the Repo members
my_permissions: TablePermission	Information about the current user permission
name: String	The Repo name
noun: String	The Repo noun for their registries
orderableFields: [String]	The orderable fields. Valid options: title, status, created_at, updated_at, finished_at
orderableTypes: [String]	The orderable field types
organization: Organization	Information about the organization
permissions: RepoPermissionsInternalGQLType	User permissions for this repo
public: Boolean	Whether the Repo is public
publicForm: PublicFormInternal	Information about the public form settings
startFormPhaseId: ID	The repo start form phase id
statuses: [TableRecordStatus]	Information about the database table statuses
summary_attributes: [SummaryAttribute]	Information about the data selected to be shown in the summarized view
summary_options: [SummaryGroup]	Information about the Repo summary options
table_fields: [TableField]	Information about the database table fields
table_records: TableRecordConnection	Fetches a group of records based on arguments
table_records_count: Int	The database table total records
title_field: TableField	Information about the field selected to be the record title
url: String	The database table URL
users_count: Int	The total users
uuid: ID
"""
connector_field="""
canConnectExisting: Boolean	Whether can connect with existing items
canConnectMultiples: Boolean	Whether is possible to connect with multiple items
canCreateNewConnected: Boolean	Whether is possible to create new connected items
connectedRepo: PublicRepoUnion	Repo (Pipe or Table) representation
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: [PublicRepoItem]	Connection field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID
"""
cpf_field = {"CpfField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	CPF field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID
"""}

currency_field = {"CurrencyField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: Float	Currency field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID
"""}

date_field = {"DateField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: Date	Date field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID
"""}

datetime_field = {"DatetimeField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: DateTime	Date time field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID
"""}

delete_organization_webhook_gql_mutation_payload = {"DeleteOrganizationWebhookGQLMutationPayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
success: Boolean	Whether the mutation was successful
"""}

due_date_field = {"DueDateField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: DateTime	Due date field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

dynamic_content_field = {"DynamicContentField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

email_attachment = {"EmailAttachment":"""
fileUrl: String	Represents the file url.
filename: String	Represents the name of the file of the attachment.
id: ID	Represents each email attachment identifier.
public_url: String	Represents the full path of the file url.
"""}

email_field = {"EmailField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Email field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

errors = {"Errors":"""
index: Int	
message: String
"""}

field_condition = {"FieldCondition":"""
actions: [FieldConditionAction]	translation missing: en.api.documentation.field_condition.actions
condition: Condition	translation missing: en.api.documentation.field_condition.condition
id: ID	translation missing: en.api.documentation.field_condition.id
isTrueFor: Boolean	translation missing: en.api.documentation.field_condition.index
name: String	translation missing: en.api.documentation.field_condition.name
phase: Phase	translation missing: en.api.documentation.field_condition.phase
"""}

field_condition_action = {"FieldConditionAction":"""

"""}

field_label = {"FieldLabel":"""
actionId: String	translation missing: en.api.documentation.field_condition_action.action
id: ID	translation missing: en.api.documentation.field_condition_action.id
phase: Phase	translation missing: en.api.documentation.field_condition_action.field
phaseField: PhaseField	translation missing: en.api.documentation.field_condition_action.field
whenEvaluator: Boolean	When condition evaluator
"""}

field_map = {"FieldMap":"""
fieldId: ID	The field ID of the father-card.
inputMode: String	How the value is going to be parsed: Valid options: - fixed_value: uses a fix value for the field. - copy_from: copies the value of the father-card.
value: String	The field ID of the child-card.
"""}

formula_field = {"FormulaField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Formula field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

help_link = {"HelpLink":"""
description: String	Represents the link description
icon: String	Represents the link icon
id: ID	Represents the link identifier
newTab: Boolean	Whether the link opens in a new tab
title: String	Represents the link title
url: String	Represents the link url
"""}

icon = {"Icon":"""
color: String	
name: String
"""}

id_field = {"IdField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
displayValue: ID	The field display value
helpText: String	The field help text
isEditable: Boolean	
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

improvement = {"Improvement":"""
app: PlatformApp	The improvement's app
clicked: Boolean	The improvement's view state
dismissed: Boolean	The improvement's dismiss state
enabled: Boolean	The improvement's view state
id: ID	Represents each improvement's identifier
link: HelpLink	The improvement's help link
viewed: Boolean	The improvement's dismiss state
"""}

improvement_setting = {"ImprovementSetting":"""
description: ID	Represents improvement setting's description
id: ID	Represents improvement setting's identifier
improvements: [Improvement]	List all improvements of an improvement setting
title: ID	Represents the improvement setting's title
"""}

inbox_email = {"InboxEmail":"""
attachments: [EmailAttachment]	Lookup the email's attachments by its identifier.
bcc: [String]	Represents Inbox Email 'BCC' email addresses.
body: String	Represents Inbox Email body, with any eventual previous replies removed.
card: Card	Lookup the card, from which the Inbox Email was sent, by its identifier.
cc: [String]	Represents Inbox Email 'CC' email addresses.
clean_html: String	Represents Inbox Email's clean HTML, only filtering the invalid or malicious characters and tags.
clean_text: String	Represents Inbox Email's clean text, only filtering the invalid or malicious characters and tags.
from: String	Represents Inbox Email sender email address.
fromName: String	Represents Inbox Email sender's name.
id: ID	Represents each email's identifier.
main_to: String	Represents Inbox Email's primary email addresses destination.
message_id: String	Represents the Inbox Email answer message identifier.
pipe: Pipe	Lookup the pipe, from which the Inbox Email was sent, by its identifier.
raw_headers: String	Represents Inbox Email raw headers.
raw_html: String	Represents Inbox Email raw HTML format, only filtering invalid characters.
sent_via_automation: Boolean	Indicates if this email was sent using an automation
state: String	Represents Inbox Email state, which can be: * 0 - Pending * 1 - Processing * 2 - Processed * 3 - Failed
subject: String	Represents Inbox Email subject.
to: [String]	Represents Inbox Email receiver email address.
updated_at: DateTime	Represents last Inbox Email update date and time.
user: User	Lookup the email's creator.
"""}

label = {"Label":"""
color: String	Represents the color used in the label using a hexadecimal string.
id: ID	Represents the label identifier.
name: String	Represents the label name.
"""}

label_field = {"LabelField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: [Label]	Label field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
labels: [Label]	Array with label information
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

long_text_field = {"LongTextField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Long text field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

member = {"Member":"""
role_name: String	The user role name Valid roles: 1. Organization: - admin: Team admin, can view/join all pipes and access/manage the team settings; - normal: Team member, can view and join all public pipes; - gest: Team guest, is free and can only create cards. 2. Pipe: - admin: Pipe admin, can create and edit cards as well as manage the pipe settings; - member: Pipe member, can create new cards as well as access the existing ones to edit and move them across the pipe; - creator: Pipe start form only, has limited access to the pipe - can create cards; - my_cards_only: Pipe restricted view, can create new cards but is only allowed to view/edit cards created by or assigned to him; - read_and_comment: Pipe read only, can view the cards and add comments. 3. Database Table: - admin: Table admin, can create an edit records, edit the table and its settings; - member: Table member, can view and create records (if authorized on the settings).
user: User	The user information
"""}

minimal_field = {"MinimalField":"""
description: String	The field description
help: String	The field help text
id: ID	The field ID
index: Float	field index
index_name: String	field index name
internal_id: ID	The field internal ID
label: String	The field title
options: [String]	The options of the Checklist, Radio or Select field
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field Universally Unique ID
"""}



number_field = {"NumberField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: Float	Number field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

organization = {"Organization":"""
billing: Billing	Organization billing infos
createdAt: DateTime	When the organization was created
createdBy: User	User that created the organization
customLogoUrl: String	The organization logo URL
freemium: Boolean	
id: ID	The organization ID
members: [Member]	Information about the organization members
membersCount: Int	Quantity of members of the organization
name: String	The organization name
onlyAdminCanCreatePipes: Boolean	Whether only Admins can create pipes
onlyAdminCanInviteUsers: Boolean	Whether only Admins can invite new users
permissions: OrganizationPermissionsInternalGQLType	User permissions for this org
pipes: [Pipe]	Fetches a group of pipes based on arguments
planName: String	
role: String	Current user's role in the organization
tables: TableConnection	Fetches a group of database tables based on arguments
userMetadata: OrganizationUserMetadata	Info on user metadata related to the current organization
users: [User]	Information about the organization users
uuid: ID	The organization UUID
webhooks: [Webhook]	Information about the organization Webhooks
"""}

organization_permissions_internal_gql_type = {"OrganizationPermissionsInternalGQLType":"""
inviteMember: Boolean	
showCompanyReports: Boolean	
showCreatePipeBanner: Boolean	
showDashboard: Boolean	
showDashboardMobile: Boolean	
showInviteMember: Boolean	
showMyTasks: Boolean	
showPortals: Boolean	
showRepoList: Boolean	
"""}

organization_user_metadata = {"OrganizationUserMetadata":"""
canCreatePipe: Boolean	Whether the user can create a new pipe
canInviteUser: Boolean	Whether the user can invite another user to this organization or not
"""}

page_info = {"PageInfo":"""
endCursor: String	When paginating forwards, the cursor to continue.
hasNextPage: Boolean	When paginating forwards, are there more items?
hasPreviousPage: Boolean	When paginating backwards, are there more items?
startCursor: String	When paginating backwards, the cursor to continue.
"""}

phase = {"Phase":"""
cards: CardConnection	Fetches a group of cards based on arguments
cards_can_be_moved_to_phases: [Phase]	Information about the phases that the cards can be moved to
cards_count: Int	The phase total cards
color: String	Color of phase
created_at: DateTime	When the phase was created
description: String	The phase description
done: Boolean	Whether it is a final phase
expiredCardsCount: Int	The phase total expired cards
fieldConditions: [FieldCondition]	Information about the phase field conditions
fields: [PhaseField]	Information about the fields
id: ID	The phase ID
index: Float	The phase positional index
isDraft: Boolean	Is this phase draft?
lateCardsCount: Int	The phase total late cards
name: String	The phase name
sequentialId: String	The sequential identifier
"""}

phase_detail = {"PhaseDetail":"""
became_late: Boolean	Whether or not the card ever became late on a phase.
created_at: DateTime	Represents the date and time of when the card first entered the phase.
draft: Boolean	Whether or not the phase detail is in the start form.
duration: Int	Represents the seconds card stayed in the phase.
firstTimeIn: DateTime	Represents the date and time of when card first entered the phase.
lastTimeIn: DateTime	Represents the date and time of when card last entered the phase.
lastTimeOut: DateTime	Represents the date and time of when card left the phase.
phase: Phase	Lookup the phase by its identifier.
"""}

phase_field = {"PhaseField":"""
allChildrenMustBeDoneToFinishParent: Boolean	Whether all child items must be done to finish the parent item
allChildrenMustBeDoneToMoveParent: Boolean	Whether all child items must be done to move the parent item
canConnectExisting: Boolean	Whether it's possible to connect existing items
canConnectMultiples: Boolean	Whether it's possible to connect multiple items
canCreateNewConnected: Boolean	Whether its possible to create new connected items
childMustExistToFinishParent: Boolean	Whether a child must exist to finish the parent
connectedRepo: PublicRepoUnion	Repo (Pipe or Table) representation
custom_validation: String	The regex used to validate the field value
description: String	The field description
editable: Boolean	Whether the field is editable in future phases
help: String	The field help text
id: ID	The field ID
index: Float	field index
index_name: String	field index name
internal_id: ID	The field internal ID
is_multiple: Boolean	Whether the field accepts multiple entries
label: String	The field title
minimal_view: Boolean	Whether the field is minimal
options: [String]	The options of the Checklist, Radio or Select field
phase: Phase	Information about the phase
required: Boolean	Whether the field is required
synced_with_card: Boolean	Whether the phase field is synchronized with the fix field
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field Universally Unique ID
"""}

phase_field_edge = {"PhaseFieldEdge":"""
cursor: String	A cursor for use in pagination.
node: PhaseField	The item at the end of the edge.
"""}

phone_field = {"PhoneField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Phone field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

pipe = {"Pipe":"""
anyone_can_create_card: Boolean	Whether anyone can create cards in the pipe
cards_count: Int	The pipe total cards
childrenRelations: [PipeRelation]	Information about the pipe child connections
clone_from_id: Int	Id which the Pipe was cloned from
color: String	Color of pipe/database
conditionExpressionsFieldIds: [Int]	IDs of all fields in a pipe that trigger conditionals
create_card_label: String	The content displayed in the start form button
created_at: DateTime	When the pipe was created
description: String	The Repo description
emailAddress: String	The pipe's email inbox address
expiration_time_by_unit: Int	The number used in the pipe SLA
expiration_unit: Int	The seconds of the unit used in the pipe SLA
fieldConditions: [FieldCondition]	Information about the fields conditions
icon: String	The Repo icon
id: ID	The pipe ID
improvementSetting: ImprovementSetting	Information about the pipe improvement setting
labels: [Label]	Information about the Repo labels
last_updated_by_card: DateTime	When a card was last updated in the pipe
members: [Member]	Information about the Repo members
name: String	The Repo name
noun: String	The Repo noun for their registries
only_admin_can_remove_cards: Boolean	Whether only Admins can delete cards
only_assignees_can_edit_cards: Boolean	Whether only the card assignees can edit it
opened_cards_count: Int	The total amount of cards not done
organization: Organization	Information about the organization
organizationId: ID	Card organization id
parentsRelations: [PipeRelation]	Information about the pipe parent connections
permissions: RepoPermissionsInternalGQLType	User permissions for this repo
phases: [Phase]	Information about the pipe phases
preferences: RepoPreference	Information about the pipe preferences
public: Boolean	Whether the Repo is public
publicForm: PublicFormInternal	Information about the public form settings
role: String	The current user role in the pipe
startFormFieldConditions: [FieldCondition]	Information about the start form fields conditions
startFormPhaseId: ID	The repo start form phase id
start_form_fields: [PhaseField]	Information about the start form fields
subtitleFields: PhaseFieldConnection	Fields used that is set as subtitle
suid: String	The pipe Small Unique ID
summary_attributes: [SummaryAttribute]	Information about the data selected to be shown in the summarized view
summary_options: [SummaryGroup]	Information about the Repo summary options
title_field: PhaseField	Information about the field selected to be the card title
users: [User]	Information about the pipe users
users_count: Int	The total users in the pipe
uuid: String	Unique identifier id
webhooks: [Webhook]	Information about the pipe Webhooks
"""}

pipe_relation = {"PipeRelation":"""
allChildrenMustBeDoneToFinishParent: Boolean	Whether all children must be done to finish the parent
allChildrenMustBeDoneToMoveParent: Boolean	Whether all children must be done to move the parent
autoFillFieldEnabled: Boolean	Whether or not the auto fill is enabled in the relation.
canConnectExistingItems: Boolean	Whether its possible to connect existing items
canConnectMultipleItems: Boolean	Whether its possible to connect multiple items
canCreateNewItems: Boolean	Whether its possible to create new connected items
child: RepoTypes	Information about the child Repo
childMustExistToFinishParent: Boolean	Whether a child must exist to finish the parent
childMustExistToMoveParent: Boolean	Whether a child must exist to move the parent
id: ID	The relation ID
name: String	The relation name
ownFieldMaps: [FieldMap]	Represents a map of fields of a parent-item to auto fill fields of a child-item's start form.
parent: RepoTypes	Information about the parent Repo
"""}

pipe_template = {"PipeTemplate":"""
icon: String	Represents the name of the icon selected to represent the template.
id: String	Represents the template identifier.
image: String	Represents the name of the image selected to represent the template.
name: String	Represents the template name.
"""}

platform_app = {"PlatformApp":"""
attachments_connection: AppAttachmentConnection	The attachments of the app for a given card
id: ID	
name: String	
public: Boolean	
slug: String	
url: String	
"""}

public_card = {"PublicCard":"""
created_at: DateTime	When the record was created
icon: Icon	Information about icon name and color
id: ID	The item ID
path: String	The item path
status: TableRecordStatus	The record status
summary: [Summary]	The item summary layout information
summary_attributes: [Summary]	Information about the repo item attributes summary layout
summary_fields: [Summary]	Information about the repo item custom fields summary layout
title: String	The item title
url: String	The URL
uuid: ID	The item uuid
"""}

public_form_internal = {"PublicFormInternal":"""
active: Boolean	Public Form is active or not
afterSubmitMessage: String	The message shown to user after submitting the public form
backgroundColor: String	The background color of the public form (RGB)
backgroundImage: String	The background image URL of the public form
brandColor: String	The brand color that will be used in the public form (RGB)
canHidePipefyLogo: Boolean	Whether the public form creator can hide Pipefy's logo
description: String	Description of the public form
displayPipefyLogo: Boolean	Whether to display Pipefy's logo in the public form
logo: String	Logo of the public form
organizationName: String	The name of the organization to be shown in the public form
reuseLastSubmissionResponse: Boolean	Fill again with the same values that were used on the last submission
showSubmitAnotherResponseButton: Boolean	Whether its allowed to submit another response
submitButtonText: String	Text of the submit button on the public form
submitterEmailCollectionEnabled: Boolean	Whether the submitter email collection is enabled
submitterEmailCollectionMethod: PublicFormSubmitterEmailCollectionMethod	The method to ask for the submitter email in the public form
submitterEmailField: MinimalField	
title: String	Title of the public form
url: String	Public form URL
"""}

public_form_settings = {"PublicFormSettings":"""
afterSubmitMessage: String	The message shown to user after submitting the public form
backgroundColor: String	The background color of the public form (RGB)
backgroundImage: String	The background image URL of the public form
brandColor: String	The brand color that will be used in the public form (RGB)
canHidePipefyLogo: Boolean	Whether the public form creator can hide Pipefy's logo
description: String	Description of the public form
displayPipefyLogo: Boolean	Whether to display Pipefy's logo in the public form
logo: String	Logo of the public form
organizationName: String	The name of the organization to be shown in the public form
public_url: String	Public form URL
reuseLastSubmissionResponse: Boolean	Fill again with the same values that were used on the last submission
showSubmitAnotherResponseButton: Boolean	Whether its allowed to submit another response
submitButtonText: String	Text of the submit button on the public form
submitterEmailCollectionEnabled: Boolean	Whether the submitter email collection is enabled
submitterEmailCollectionMethod: PublicFormSubmitterEmailCollectionMethod	The method to ask for the submitter email in the public form
submitterEmailField: MinimalField	
title: String	Title of the public form
"""}

public_pipe = {"PublicPipe":"""
createButtonLabel: String	The creation button label
icon: String	The Repo icon
id: ID	The pipe ID
name: String	The Repo name
uuid: ID	The Repo UUID
"""}

public_repo_item = {"PublicRepoItem":"""
created_at: DateTime	When the record was created
icon: Icon	Information about icon name and color
id: ID	The item ID
path: String	The item path
status: TableRecordStatus	The record status
summary: [Summary]	The item summary layout information
summary_attributes: [Summary]	Information about the repo item attributes summary layout
summary_fields: [Summary]	Information about the repo item custom fields summary layout
title: String	The item title
url: String	The URL
uuid: ID	The item uuid
"""}

public_table = {"PublicTable":"""
color: String	Color of database
createButtonLabel: String	The creation button label
icon: String	The Repo icon
id: ID	The table ID
internal_id: ID	The internal table ID
name: String	The Repo name
uuid: ID	The Repo UUID
"""}

public_table_record = {"PublicTableRecord":"""
created_at: DateTime	When the record was created
icon: Icon	Information about icon name and color
id: ID	The item ID
path: String	The item path
status: TableRecordStatus	The record status
summary: [Summary]	The item summary layout information
summary_attributes: [Summary]	Information about the repo item attributes summary layout
summary_fields: [Summary]	Information about the repo item custom fields summary layout
title: String	The item title
url: String	The URL
uuid: ID	The item uuid
"""}

public_table_record_edge = {"PublicTableRecordEdge":"""
cursor: String	A cursor for use in pagination.
node: PublicTableRecord	The item at the end of the edge.
"""}

public_user = {"PublicUser":"""
avatarUrl: String	The user's avatar URL
email: String	The user email
id: ID	The user ID
name: String	The user name
username: String	The user username
"""}

query = {"Query":"""
allCards: CardConnection	Fetches all pipe cards based on arguments
autoFillFields: [AutoFillFieldUnion]	Lookup the values that will automatically fill the child-card's start form fields
card: Card	Lookup a card by its ID
cards: CardConnection	Fetches a group of cards based on arguments
cardsImportations: [CardsImportation]	Lookup the cards importer history by the pipe ID
conditionalField: ConditionalField	
connectedTableRecords: PublicTableRecordConnection	
fieldCondition: FieldCondition	
findCards: CardConnection	Fetch cards based on fields' inputs
findRecords: CardConnection	Fetch records based on fields' inputs
inbox_emails: [InboxEmail]	Lookup the card's emails by its ID
me: User	Returns informations of the current authenticated user
organization: Organization	Lookup an organization by its ID
organizations: [Organization]	Lookup organizations by their ID
phase: Phase	Lookup a phase by its ID
pipe: Pipe	Lookup a pipe by its ID
pipe_relations: [PipeRelation]	Lookup pipe relations by their ID
pipe_templates: [PipeTemplate]	Lookup all pipe templates available on Pipefy
pipes: [Pipe]	Lookup pipes by their ID
recordsImportations: [RecordsImportation]	Lookup the records importer history by the table ID
repoItemForm: RepoItemFormUnion	
table: Table	Lookup a database table by its ID
table_record: TableRecord	Lookup a record by its ID
table_records: TableRecordWithCountConnection	Fetches a group of records based on arguments
table_relations: [TableRelation]	Lookup table relations by their ID
tables: [Table]	Lookup database tables by their ID
"""}

radio_horizontal_field = {"RadioHorizontalField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Horizontal radio field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
options: [String]	The horizontal radio options
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

radio_vertical_field = {"RadioVerticalField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Vertical radio field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
options: [String]	The vertical radio options
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

records_importation = {"RecordsImportation":"""
createdAt: DateTime	The importation date of creation
createdBy: User	The importation creator
dateFormatted: String	The importation date of creation formatted
id: ID	The importation ID
importedRecords: Int	The amount of records imported
status: String	The importation status
url: String	The xlsx file URL
"""}

remove_user_from_org_payload = {"RemoveUserFromOrgPayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
success: Boolean	Whether the mutation was successful
"""}

remove_user_from_pipe_payload = {"RemoveUserFromPipePayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
success: Boolean	Whether the mutation was successful
"""}

remove_user_from_table_payload = {"RemoveUserFromTablePayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
success: Boolean	Whether the mutation was successful
"""}

repo_item_types_edge = {"RepoItemTypesEdge":"""
cursor: String	A cursor for use in pagination.
node: RepoItemTypes	The item at the end of the edge.
"""}

repo_permissions_internal_gql_type = {"RepoPermissionsInternalGQLType":"""
configure_repo: Boolean	
create_item: Boolean	
delete_item: Boolean	
delete_repo: Boolean	
manage_field: Boolean	
manage_label: Boolean	
show_repo: Boolean	
"""}

repo_preference = {"RepoPreference":"""
enableExternalGuests: Boolean	External guests can or cannot create cards on this pipe
hiddenStartFormAttributes: [String]	Represents the attributes selected to be hidden in the start form.
hiddenTopButtons: [String]	Represents the top buttons selected to be hidden in the open card.
inboxEmailEnabled: Boolean	Whether or not the email client is enabled.
mainTabViews: [String]	Represents the views selected to be shown in the card.
startFormTitle: String
"""}

select_field = {"SelectField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Select field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
options: [String]	The select options
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

send_inbox_email_payload = {"SendInboxEmailPayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
success: Boolean	Whether the mutation was successful
"""}

set_role_payload = {"SetRolePayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
member: Member	Returns information about the member
"""}

short_text_field = {"ShortTextField":"""
customValidation: String	The short text field custom validation
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Short text field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

statement_field = {"StatementField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
uuid: ID	The field universally unique ID
"""}

summary = {"Summary":"""
title: String	Represents the title of the selected field to be represented in the summary.
type: String	Field type
value: String	Represents the value of the selected field to be represented in the summary.
"""}

summary_attribute = {"SummaryAttribute":"""
id: String	Represents summary attribute identifier. 
    It accepts the field's internal identifier or the repository attribute's slug. 
    Valid repository attribute's options:
    - id - title - current_phase - labels - due_date - created_by 
    - assignees - finished_at - created_at - status - updated_at 
    - last_comment - last_comment_at
"""}

summary_group = {"SummaryGroup":"""
name: String	Represents a general information of a card or a phase's field.
options: [SummaryOption]	Lookup the summary group options by its identifier.
"""}

summary_option = {"SummaryOption":"""
id: String	Represents the field's internal identifier or the card attribute's slug.
label: String	Represents the summary option title label.
"""}

table = {"Table":"""
anyone_can_create_card: Boolean	Allows anyone to create cards
authorization: TableAuthorization	Information about the database table authorization
color: String	Color of pipe/database
conditionExpressionsFieldIds: [Int]	IDs of all fields in a pipe that trigger conditionals
create_record_button_label: String	The content displayed in the start form button
description: String	The Repo description
icon: String	The Repo icon
id: ID	The database table ID
internal_id: ID	The database table internal ID
labels: [Label]	Information about the Repo labels
members: [Member]	Information about the Repo members
my_permissions: TablePermission	Information about the current user permission
name: String	The Repo name
noun: String	The Repo noun for their registries
orderableFields: [String]	The orderable fields. Valid options: title, status, created_at, updated_at, finished_at
orderableTypes: [String]	The orderable field types
organization: Organization	Information about the organization
permissions: RepoPermissionsInternalGQLType	User permissions for this repo
public: Boolean	Whether the Repo is public
publicForm: PublicFormInternal	Information about the public form settings
startFormPhaseId: ID	The repo start form phase id
statuses: [TableRecordStatus]	Information about the database table statuses
summary_attributes: [SummaryAttribute]	Information about the data selected to be shown in the summarized view
summary_options: [SummaryGroup]	Information about the Repo summary options
table_fields: [TableField]	Information about the database table fields
table_records: TableRecordConnection	Fetches a group of records based on arguments
table_records_count: Int	The database table total records
title_field: TableField	Information about the field selected to be the record title
url: String	The database table URL
users_count: Int	The total users
uuid: ID	The database uuid
webhooks: [Webhook]	Information about the table Webhooks
"""}

table_edge = {"TableEdge":"""
cursor: String	A cursor for use in pagination.
node: Table	The item at the end of the edge.
"""}

table_field = {"TableField":"""
allChildrenMustBeDoneToFinishParent: Boolean	Whether all child items must be done to finish the parent item
canConnectExisting: Boolean	Whether it's possible to connect existing items
canConnectMultiples: Boolean	Whether it's possible to connect multiple items
canCreateNewConnected: Boolean	Whether its possible to create new connected items
childMustExistToFinishParent: Boolean	Whether a child must exist to finish the parent
connectedRepo: PublicRepoUnion	Repo (Pipe or Table) representation
custom_validation: String	The regex used to validate the field value
description: String	The field description
help: String	The field help text
id: ID	The field ID
index: Float	field index
index_name: String	field index name
internal_id: ID	The field internal ID
is_multiple: Boolean	Whether the field accepts multiple entries
label: String	The field title
minimal_view: Boolean	Whether the field is minimal
options: [String]	The options of the Checklist, Radio or Select field
required: Boolean	Whether the field is required
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field must have a unique value
uuid: ID	The field Universally Unique ID
"""}

table_permission = {"TablePermission":"""
can_manage_record: Boolean	Whether or not user can create, edit and delete records in the database table.
can_manage_table: Boolean	Whether or not user can edit and delete the database table (Admin).
"""}

table_record = {"TableRecord":"""
assignees: [User]	Information about the assign users
created_at: DateTime	When the record was created
created_by: User	Information about the record creator
done: Boolean	Whether the record is done
due_date: DateTime	The record due date
finished_at: DateTime	When the record was finished
id: ID	The record ID
labels: [Label]	Information about the record labels
parent_relations: [TableRecordRelation]	Information about the parent table connections
path: String	The record path
record_fields: [TableRecordField]	Information about the record fields
status: TableRecordStatus	The record status
summary: [Summary]	Information about the record summary layout
summary_attributes: [Summary]	Information about the card attributes summary layout
summary_fields: [Summary]	Information about the card custom fields summary layout
table: Table	Information about the database table
title: String	The record title
updated_at: DateTime	When the record was last updated
url: String	The URL
uuid: ID	The record uuid
"""}

table_record_edge = {"TableRecordEdge":"""
cursor: String	A cursor for use in pagination.
node: TableRecord	The item at the end of the edge.
"""}

table_record_field = {"TableRecordField":"""
array_value: [String]	The value of an Attachment, Checklists, Connection or Label field, processed as an array type
assignee_values: [User]	Information about the users assigned to the card
connectedRepoItems: [PublicRepoItemTypes]	Information about cards and records connected with the card
date_value: Date	The value of a Date, DateTime or DueDate field, processed as a date type
datetime_value: DateTime	The value of a DateTime or DueDate field, processed as a date and time type
field: MinimalField	Information about the card field
filled_at: DateTime	When the field was filled
float_value: Float	The field float value
indexName: String	The searcheable name
label_values: [FieldLabel]	Information about the card label
name: String	The field name
phase_field: PhaseField	Information about the field's phase
report_value: String	The field value prepared for report
required: Boolean	Whether or not the record's field is required.
updated_at: DateTime	When the field was last updated
value: String	The field value
"""}

table_record_form = {"TableRecordForm":"""
createButtonLabel: String	The creation button label
formFields: [RepoItemFieldsTypes]	The available fields in Pipefy
icon: String	The Repo icon
id: ID	
name: String	The Repo name
uuid: ID	The Repo UUID
"""}

table_record_relation = {"TableRecordRelation":"""
id: ID	Represents a relation's id.
name: String	Represents a relation's name.
repo: TableConnectedRepoGQLCoreUnionTypes	Represents a repo (Card or Table Record).
repo_items: RepoItemTypesConnection	Fetches a group of records based on arguments.
source_type: String	Represents the type source. It can be a database table or a pipe.
"""}

table_record_status = {"TableRecordStatus":"""
id: ID	Represents the status identifier.
name: String	Represents the status name.
"""}

table_relation = {"TableRelation":"""
allChildrenMustBeDoneToFinishParent: Boolean	Whether all children must be done to finish the parent
allChildrenMustBeDoneToMoveParent: Boolean	Whether all children must be done to move the parent
canConnectExistingItems: Boolean	Whether its possible to connect existing items
canConnectMultipleItems: Boolean	Whether its possible to connect multiple items
canCreateNewItems: Boolean	Whether its possible to create new connected items
child: RepoTypes	Information about the child Repo
childMustExistToFinishParent: Boolean	Whether a child must exist to finish the parent
childMustExistToMoveParent: Boolean	Whether a child must exist to move the parent
id: ID	The relation ID
name: String	The relation name
parent: RepoTypes	Information about the parent Repo
"""}

time_field = {"TimeField":"""
description: String	The field description
displayState: ConditionFieldActions	The field current state
helpText: String	The field help text
initialValue: String	Time field initial value
isEditable: Boolean	If the field could be editable
isRequired: Boolean	Whether the field is required
label: String	The field title
minimalView: Boolean	Whether the field is minimal
triggersFieldConditions: Boolean	Whether the field triggers a condition
type: String	The field type. Valid options: assignee_select, attachment, checklist_horizontal, checklist_vertical, cnpj, connector, cpf, currency, date, datetime, due_date, email, id, label_select, long_text, number, phone, radio_horizontal, radio_vertical, select, short_text, statement, time, formula, dynamic_content
unique: Boolean	Whether the field value must be unique
uuid: ID	The field universally unique ID
"""}

update_fields_values_payload = {"UpdateFieldsValuesPayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
success: Boolean	Return if the mutation ran succesfully or not.
updatedNode: UpdatedNode	The updated card or table record.
userErrors: [[ID]]	List of errors that occurred executing the mutation.
"""}

update_organization_webhook_payload = {"UpdateOrganizationWebhookPayload":"""
clientMutationId: String	A unique identifier for the client performing the mutation.
webhook: Webhook	Returns information about the webhook
"""}

user = {"User":"""
avatarUrl: String	The user avatar URL
confirmationTokenHasExpired: Boolean	Whether the user confirmation token expired and is no longer valid
confirmed: Boolean	Whether the user is confirmed or not
createdAt: String	When the user was created
departmentKey: String	The user department key
displayName: String	The user display name
email: String	The user email
hasUnreadNotifications: Boolean	Returns if the user has unread notifications
id: ID	The user ID
intercomHash: String	Return the hash reference for intercom
intercomId: ID	The user intercom reference
invited: Boolean	Whether the user was invited to register or not
locale: String	The user language
name: String	The user name
phone: String	The user's phone
preferences: UserPreference	The user preferences
signupData: String	The user template category key
timezone: String	The user time zone
username: String	The user username
uuid: ID	The user UUID
"""}

user_error = {"UserError":"""
field: [[ID]]	Path to the input field which caused the error.
message: String	The error message.
"""}

user_preference = {"UserPreference":"""
browserNativeNotificationEnabled: Boolean	Whether the user notification is enable or not
displayImprovements: Boolean	Whether the improvements are visible or not
displayOrganizationReportSidebar: Boolean	Represents organization reports sidebar status (hide or show) of an user.
displayPipeReportsSidebar: Boolean	Whether the Pipe Reports Sidebar is visible or not
favoritePipeIds: [Int]	List of pipes (by id) favourited by the user
openNestedStartForm: Boolean	Whether the startform open in a modal or inside open card
sidebarOpened: Boolean	Whether the sidebar is opened or not
suggestedTemplatesClosed: Boolean	Whether the user closed the suggested templates box
useNewOpenCard: Boolean	Whether the use new open card or not
"""}

webhook = {"Webhook":"""
actions: [String]	The webhook triggers. Valid options: card.create, card.done, card.expired, card.late, card.move, card.overdue, card.field_update, user.removal_from_org, user.removal_from_pipe, user.removal_from_table, user.role_set, user.invitation_acceptance, user.invitation_sent
email: String	The webhook chosen email
headers: Json	The webhook custom headers
id: ID	The webhook ID
name: String	The webhook name
url: String	The webhook URL
"""}

__directive = {"__Directive":"""
  A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document. In some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor.
args: [ID]	
description: String	
locations: [ID]	
name: String
"""}

__enum_value = {"__EnumValue":"""
deprecationReason: String	
description: String	
isDeprecated: Boolean	
name: String
"""}

__field = {"__Field":"""
args: [ID]	
deprecationReason: String	
description: String	
isDeprecated: Boolean	
name: String	
type: __Type
"""}

__input_value = {"__InputValue":"""
defaultValue: String	A GraphQL-formatted string representing the default value for this input value.
description: String	
name: String	
type: __Type
"""}

__schema = {"__Schema":"""
directives: [ID]	A list of all directives supported by this server.
mutationType: __Type	If this server supports mutation, the type that mutation operations will be rooted at.
queryType: __Type	The type that query operations will be rooted at.
subscriptionType: __Type	If this server support subscription, the type that subscription operations will be rooted at.
types: [ID]	A list of all types supported by this server.
"""}

__Type = {"__Type":"""
description: String	
enumValues: [[ID]]	
fields: [[ID]]	
inputFields: [[ID]]	
interfaces: [[ID]]	
kind: __TypeKind	
name: String	
ofType: __Type	
possibleTypes: [[ID]]
"""}
 

























































































