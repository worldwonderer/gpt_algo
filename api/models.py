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


class SystemDesign(Document):
    _id = StringField(required=True, primary_key=True)
    description = StringField(required=True)
    difficulty = StringField(required=True)
    problem_path_name = StringField(db_field='problemPathName', required=True)
    title = StringField(required=True)
    description_zh = StringField()
    title_zh = StringField()

    meta = {
        'collection': 'system_design'
    }


class Diagram(EmbeddedDocument):
    value = StringField()

    meta = {
        'strict': False
    }


class DiagramCode(EmbeddedDocument):
    highlevel = EmbeddedDocumentField(Diagram)
    er = EmbeddedDocumentField(Diagram)
    sequence = EmbeddedDocumentField(Diagram)
    class_diagram = EmbeddedDocumentField(Diagram, db_field='classDiagram')
    state = EmbeddedDocumentField(Diagram)

    meta = {
        'strict': False
    }


class SolutionSection(EmbeddedDocument):
    name = StringField()
    title = StringField()
    placeholder = StringField()
    content = StringField()

    meta = {
        'strict': False
    }


class Solution(EmbeddedDocument):
    diagram_code = EmbeddedDocumentField(DiagramCode, db_field='diagramCode')
    sections = ListField(EmbeddedDocumentField(SolutionSection))
    sections_zh = ListField(EmbeddedDocumentField(SolutionSection), db_field='sections_zh')

    meta = {
        'strict': False
    }


class SystemDesignSolution(Document):
    _id = StringField(required=True, primary_key=True)
    created_at = StringField(db_field='createdAt', required=True)
    id_path = StringField(db_field='idPath', required=True)
    score = IntField(required=True)
    solution = EmbeddedDocumentField(Solution)
    problem_path_name = StringField(db_field='problemPathName', required=True)

    meta = {
        'collection': 'system_design_solution',
        'strict': False
    }
