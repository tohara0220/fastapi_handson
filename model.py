from pydantic import BaseModel


class Task(BaseModel):
    """
    「プロパティ：データ型」の形式とする。
    イコールで繋ぐことでデフォルト値になる
    クラス単位で型定義を行う。Typescriptのように関数の引数で型定義をするわけではない。型定義をするタイミングは言語で異なる。
    """

    title: str
    description: str = None
    completed: bool = False
