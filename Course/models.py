from django.db import models

# Create your models here.


class ListField(models.CharField):
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_db_prep_value(self, value, connection=None, prepared=False):
        if isinstance(value, str):
            return value
        elif isinstance(value, list):
            return ",".join(value)

    def to_python(self, value):
        print('*' * 50)
        print(value)
        # if value is not None:
        #     return value if isinstance(value, list) else value.split(',')
        # return []
        return value

    # def get_prep_lookup(self, lookup_type, value):
    #     """限制查询方式"""
    #     print(value)
    #     if lookup_type == 'exact':
    #         return value
    #     elif lookup_type == 'in':
    #         print([self.get_prep_value(v) for v in value])
    #         return [self.get_prep_value(v) for v in value]
    #     else:
    #         return TypeError('lookup type %r not supported' % lookup_type)


class TermInfo(models.Model):
    term_name = models.CharField(max_length=50, verbose_name='学期名称')
    start_date = models.DateField(verbose_name='学期开始日期')
    end_date = models.DateField(verbose_name='学期结束日期')
    week_counts = models.IntegerField(verbose_name='学期总周数', default=20)
    # current_week = models.IntegerField(verbose_name='当前周数', default=1)

    class Meta:
        db_table = 'TermInfo'
        verbose_name = '学期'
        verbose_name_plural = "学期管理"

    def __str__(self):
        return self.term_name


class Teacher(models.Model):
    name = models.CharField(max_length=25, verbose_name='姓名')
    gender_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.IntegerField(choices=gender_choices, blank=True, null=True, verbose_name='性别')

    class Meta:
        db_table = 'Teacher'
        verbose_name = '教师'
        verbose_name_plural = "教师管理"

    def __str__(self):
        return self.name


class Course(models.Model):
    # 归属学期
    # term = models.ForeignKey(TermInfo, on_delete=models.SET_NULL, blank=True, null=True)
    # 科目名
    course_name = models.CharField(max_length=50, verbose_name='课程名称')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='教师姓名', default=None)
    # 考核方式
    assessment_method_choices = (
        ('考试', '考试'),
        ('考查', '考查')
    )
    assessment_method = models.CharField(max_length=10, choices=assessment_method_choices, verbose_name='考核方式')

    class Meta:
        db_table = 'Course'
        verbose_name = '课程'
        verbose_name_plural = "课程名称管理"

    def __str__(self):
        return self.course_name


class LessonSchedule(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    start_time = models.TimeField(verbose_name='上课时间')
    end_time = models.TimeField(verbose_name='下课时间')

    class Meta:
        db_table = 'LessonSchedule'
        verbose_name = '作息时间表'
        verbose_name_plural = "作息时间表管理"

    def __str__(self):
        return self.title


class ClassSchedule(models.Model):
    # 当课程删除时，自动删除
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程名称')
    # 星期几
    week_day_choices = (
        (1, '星期一'),
        (2, '星期二'),
        (3, '星期三'),
        (4, '星期四'),
        (5, '星期五'),
        (6, '星期六'),
        (0, '星期日')
    )
    week_day = models.IntegerField(choices=week_day_choices, verbose_name='星期几')
    # 教室
    classroom = models.CharField(max_length=50, verbose_name='教室')
    # 周次
    weeks = ListField(max_length=256, verbose_name='周次')
    # 节次
    lesson = models.ForeignKey(LessonSchedule, on_delete=models.CASCADE, verbose_name='节次')
    # 是否停课
    is_suspend = models.BooleanField(default=False, verbose_name='是否停课')

    class Meta:
        db_table = 'ClassSchedule'
        verbose_name = '课程表'
        verbose_name_plural = "课程表管理"

    def __str__(self):
        return ' | '.join([str(self.course), str(self.get_week_day_display()), str(self.lesson)])





