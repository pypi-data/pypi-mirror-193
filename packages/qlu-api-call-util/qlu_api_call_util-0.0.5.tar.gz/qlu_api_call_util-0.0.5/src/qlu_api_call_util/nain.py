from api_call import create_async_post_request
import asyncio
import time

url = 'https://qlurec-nlp-utils-clustering-spec-bdhweedyzq-uc.a.run.app'
data_dict = {"specialties": ["machine learning", "artificial intelligence", "computer vision", "natural language processing", "employee consulting", "professional resourcing", "higher ed", "training and development", "graduate", "undergraduate"]}


def main():
    print('first')
    task = create_async_post_request(url=url, data_dict=data_dict)
    time.sleep(2)
    print('Hello')

    print('h2')
    print(task.get())
    print('end')

if __name__ == "__main__":
    main()


