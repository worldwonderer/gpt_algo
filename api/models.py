from mongoengine import Document, StringField, IntField, BooleanField, ListField, EmbeddedDocument, \
    EmbeddedDocumentField, DictField


class TimeComplexity(EmbeddedDocument):
    analysis = StringField()
    result = StringField()


class SpaceComplexity(EmbeddedDocument):
    analysis = StringField()
    result = StringField()


class Explain(EmbeddedDocument):
    approach = StringField()
    timeComplexity = EmbeddedDocumentField(TimeComplexity)
    spaceComplexity = EmbeddedDocumentField(SpaceComplexity)
    code = StringField()


class Submission(EmbeddedDocument):
    submission_id = IntField()
    lang = StringField()
    language = StringField()
    memory = StringField()
    runtime = StringField()
    timestamp = StringField()
    code = StringField()
    is_mine = BooleanField()


class Explore(EmbeddedDocument):
    content = StringField()
    explanation = StringField()


class Problem(Document):
    _id = StringField(primary_key=True)
    ac_rate = StringField()
    content_cn = StringField()
    content_en = StringField()
    difficulty = IntField()
    explain = EmbeddedDocumentField(Explain)
    frontend_id = StringField()
    paid_only = BooleanField()
    similar_questions = ListField(StringField())
    submission = EmbeddedDocumentField(Submission)
    tags_q = ListField(StringField())
    tags = DictField()
    title_cn = StringField()
    title_en = StringField()
    title_slug = StringField()
    total_acs = IntField()
    total_submitted = IntField()
    explore = ListField(EmbeddedDocumentField(Explore))

    meta = {'collection': 'leetcode'}
