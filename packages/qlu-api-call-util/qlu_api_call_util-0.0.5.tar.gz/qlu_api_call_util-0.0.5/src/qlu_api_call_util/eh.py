import json
import time
from qlu_api_call_util import make_api_request_async
# from qlu_api_call_util import make_multiple_api_requests_async
# from qlu_api_call_util import create_task_post_api_request_call
from asyncio import create_task, run
from multiprocessing.pool import ThreadPool
import time


def convert_call_to_async(coroutine_to_exec):
    # t1 = threading.Thread(target=run, args=(coroutine_to_exec,))
    # t1.start()
    pool = ThreadPool(processes=1)
    async_call = pool.apply_async(run, (coroutine_to_exec,))
    return async_call


def main():
    st_time = time.time()
    TASK = make_api_request_async('https://yori-qa-flan-chatgpt3-v3-bdhweedyzq-uc.a.run.app', data_dict={"context": " Muhammad Musa Chughtai is a Mechanical Engineering graduate from Ghulam Ishaq Khan Institute of Engineering Sciences and Technology.Muhammad Musa Chughtai is currently working at QLU.ai, a Computer Softwarecompany specializing in Artificial Intelligence, Recruitment, Automation, NLP with 34 employees.Muhammad Musa Chughtai's title on LinkedIn is Full Stack - QLU | GIKI-22.Muhammad Musa Chughtai is skilled in Networking, Web Development, Instrumentation, Operations Management, Debate, JavaScript, Node.js, SQL, React.js, SCSS, Digital Marketing, Adobe Photoshop, Full-Stack Development, Systems Analysis, Engineering. Muhammad Musa Chughtai worked as a Full Stack Engineer at QLU.ai, a company specializing in Artificial Intelligence, Recruitment, Automation, NLP. The role started in 11-2022, until Present lasting for 4 months. QLU.ai has a team size of 34. Before that, Muhammad Musa Chughtai worked as a Junior Quality Assurance Engineer at QLU.ai. The role started in 6-2022, until 11-2022 lasting for 6 months. Before that, Muhammad Musa Chughtai worked as a Head Of Web Development at GIK Institute Consulting Group . Muhammad Musa Chughtaiwrote his role description as: \"Managing and Consulting for improvements for the website of GIK Consulting Group\". Therole started in 8-2021, until 5-2022 lasting for 10 months. Before that, Muhammad Musa Chughtai worked as a Treasurer at NETRONiX. Muhammad Musa Chughtai wrote his role description as: \"Handling and maintaining financial log books of NETRONIX\". The role started in 5-2021, until 5-2022 lasting for 1 yr 1 month. Before that, Muhammad Musa Chughtai worked as a Full Stack Intern at QLU.ai. Muhammad Musa Chughtai wrote his role description as: \"Training and working with the Full-Stack team at the startup while learning and using ReactJS\". The role started in 7-2021, until 12-2021 lasting for 6 months in Islāmābād, Pakistan. Muhammad Musa Chughtai graduated from Ghulam Ishaq Khan Institute of Engineering Sciences and Technology doing Bachelor of Science - BSc in Mechanical Engineering between 2018 and 2022. ", "question": "Where does he work?"}, header_dict={
                                  'Content-Type': 'application/json'}, retries=3, duration_before_retry=[1, 2, 3], verbose=True)
    # TASK = create_task(TASK)

    TASK = convert_call_to_async(TASK)

    print("REAL HABIBI!!!")


    time.sleep(2)

    print("NON REAL HABIBI!!")

    # value =  await TASK
    print("HABIBI HAYA HAYA!!!!")
    value = TASK.get()
    print(value)

    print(TASK)
    end_time = time.time()
    print(f'Total time taken {end_time-st_time} seconds ')

if __name__ == "__main__":

    # run(main())
    main()