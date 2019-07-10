from sqlalchemy.orm import class_mapper


def serialize(model):
    """
    序列化查询集或单个查询对象
    :param model:
    :return:
    """
    if isinstance(model, list):
        _list = []
        for i in model:
            columns = [c.key for c in class_mapper(i.__class__).columns]
            _list.append(dict((c, getattr(i, c)) for c in columns))
        return _list
    else:
        columns = [c.key for c in class_mapper(model.__class__).columns]
        return dict((c, getattr(model, c)) for c in columns)
