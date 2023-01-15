#!/usr/bin/env python

import argparse
from dataclasses import dataclass
import datetime
import operator
import random
import sys


@dataclass
class JobInfo:

    id: int
    start_time: datetime.datetime
    user: str
    walltime: int
    exit_status: int

    @staticmethod
    def attributes():
        return ['id', 'start_time', 'user', ',walltime', 'exit_status']

    def __repr__(self):
        return f'{self.id},{self.start_time.strftime("%Y-%m-%d %H:%M:%S")},{self.user},{self.walltime},{self.exit_status}'


def generate_timestamp(options):
    start = datetime.datetime(*map(int, options.start_date.split('-')))
    end = datetime.datetime(*map(int, options.end_date.split('-')))
    date = start + datetime.timedelta(random.randrange(0, (end - start).days))
    hours = random.randrange(0, 24)
    minutes = random.randrange(0, 60)
    seconds = random.randrange(0, 60)
    date += datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return date

def generate_job(job_id, options):
    return JobInfo(
        id=job_id,
        start_time=generate_timestamp(options),
        user=f'vsc30{random.randint(1, options.nr_users):03d}',
        walltime=random.randint(1, options.max_walltime),
        exit_status=random.choices([0, 1], weights=(options.success_rate, 1.0 - options.success_rate))[0],
    )

def validate_args(options):
    if options.nr_jobs <= 0:
        raise ValueError('number of jobs must be at least 1')
    if options.nr_users <= 0:
        raise ValueError('number of users must be at least 1')
    if options.success_rate < 0.0 or options.success_rate > 1.0:
        raise ValueError('success rate must be between 0.0 and 1.0')
    if options.max_walltime <= 0:
        raise ValueError('maximum walltime of jobs must be at least 1 second')
    start = datetime.datetime(*map(int, options.start_date.split('-')))
    end = datetime.datetime(*map(int, options.end_date.split('-')))
    if end <= start:
        raise ValueError('end date must be later than start date')
    if options.jobid_offset < 0:
        raise ValueError('job ID offset should be positive')



def main():
    arg_parser = argparse.ArgumentParser(description='data generator')
    arg_parser.add_argument('--nr-jobs', type=int, default=50,
                            help='number of jobs')
    arg_parser.add_argument('--nr-users', type=int, default=10,
                            help='number of users')
    arg_parser.add_argument('--success_rate', type=float, default=0.9,
                            help='success rate of jobs')
    arg_parser.add_argument('--max-walltime', type=int, default=3600,
                            help='maximum walltime')
    arg_parser.add_argument('--start-date', default='2022-01-01',
                            help='first log date')
    arg_parser.add_argument('--end-date', default='2022-03-01',
                            help='last log date')
    arg_parser.add_argument('--jobid-offset', type=int, default=0,
                            help='offset for job IDs')
    options = arg_parser.parse_args()
    try:
        validate_args(options)
    except ValueError as error:
        print(f'### error: invalid argument, {error}', file=sys.stderr)
        return 1
    print(','.join(JobInfo.attributes()))
    job_iter = (generate_job(job_id, options)
                for job_id in range(1, options.nr_jobs + 1))
    for job_id, job_info in enumerate(sorted(job_iter,
                                             key=operator.attrgetter('start_time'))):
        job_info.id = job_id + 1 + options.jobid_offset
        print(job_info)
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
