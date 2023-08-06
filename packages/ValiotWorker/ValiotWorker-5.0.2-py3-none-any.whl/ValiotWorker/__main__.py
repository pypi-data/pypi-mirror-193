import os
from pprint import pprint
from pygqlc import GraphQLClient
from .worker import ValiotWorker, QueueType, PollingMode, JobConfigMode, LogLevel
# ! Create main helpers:
gql = GraphQLClient()
vw = ValiotWorker()
# * Initialize helpers:
gql.addEnvironment(
    'dev',
    url=os.environ.get('API'),
    wss=os.environ.get('WSS'),
    headers={'Authorization': os.environ.get('TOKEN')},
    default=True)
vw.setClient(gql)
vw.setWorker(os.environ.get('WORKER'))
vw.setPollingMode(PollingMode.SUBSCRIPTION)
vw.setJobConfigMode(JobConfigMode.SYNC)


@vw.job(
    name='TEST_JOB',
    alias='test job 1',
    description='',
    schedule='* * * * *',
    enabled=True,
    queueType=QueueType.FREQUENCY,
)
def test_job(**_):
    print("Hi, I'm test job #1")
    return {'result': 'ok 1'}


@vw.job(
    name='TEST_JOB_SIMPLE_OUTPUT',
    alias='test job simple output',
    description='',
    enabled=True,
    queueType=QueueType.ON_DEMAND,
)
def test_job(**_):
    print("Hi, I'm test job simple output")
    return 'ok simple output'

@vw.job(
    name='TEST_JOB_2',
    alias='test job 2',
    description='',
    schedule='*/3 * * * *',
    enabled=True,
    queueType=QueueType.FREQUENCY,
)
def test_job_2(log, **_):
    log(LogLevel.INFO, "Hi, I'm test job #2")
    return {'result': 'ok 2'}

@vw.job(
    name='TEST_JOB_THAT_FAILS',
    alias='test job that fails',
    description='',
    enabled=True,
    queueType=QueueType.ON_DEMAND,
)
def test_job_that_fails(log, **_):
    log(LogLevel.INFO, "Hi, I'm test job #3")
    raise Exception('This job fails')

def main():
    print('main for valiot worker')
    vw.run(interval=5.0)


if __name__ == "__main__":
    main()
