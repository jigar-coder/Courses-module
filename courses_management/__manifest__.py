# -*- encoding: utf-8 -*-
{
    'name': "Courses Management",
    'category': 'e-learn',
    'version': '1.0',
    'author': 'Jigar Sorathiya',
    'maintainer': 'Jigar Sorathiya',
    'summary': """
    Manage  Courses.
    """,
    'author': "Jigar Sorathiya",
    'description': """
        From eLearning menu user can create the courses.
        and in that create the lessons.
        to set the  instructor of courses need to go to options tab and set
        Instructor.
    """,
    'depends': ['website_slides', 'hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_slides_channel_form_inherit.xml',
        'views/view_lessons_rooms.xml',
        'views/hr_contract_view_form_inherit.xml',
        'report/courses_template.xml',
        ],
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
}
