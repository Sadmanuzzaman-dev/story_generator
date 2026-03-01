from typing import List
from pydantic_settings import BaseSettings #BaseSettings হলো একটা স্পেশাল ক্লাস যেটা .env ফাইল থেকে অটোমেটিক ভ্যালু পড়ে আনে।
from pydantic import field_validator #


"""
এই ফাইলটি আমাদের অ্যাপ্লিকেশন এর কনফিগারেশন সেটিংস সংরক্ষণ করে। আমরা এখানে API এর প্রিফিক্স, ডিবাগ মোড, ডাটাবেস URL,
অনুমোদিত উৎস এবং OpenAI API key সংজ্ঞায়িত করেছি। এই সেটিংসগুলি .env ফাইল থেকে পড়া হয় এবং অ্যাপ্লিকেশন জুড়ে ব্যবহার 
করা হয়। এটি আমাদের কোডকে আরও পরিষ্কার এবং পরিচালনাযোগ্য করে তোলে, কারণ আমরা কনফিগারেশন মানগুলি এক জায়গায় 
সংরক্ষণ করতে পারি এবং প্রয়োজন অনুযায়ী পরিবর্তন করতে পারি।          
"""

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str 
    ALLOW_ORIGINS: str = ""
    OPENAI_API_KEY: str = ""

    @field_validator("ALLOW_ORIGINS")
    def parse_allow_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()


