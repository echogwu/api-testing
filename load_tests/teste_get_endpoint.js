import { check } from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<200'], // 95% of requests should be below 200ms
    },
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 300, // number of constant iterations given `timeUnit`. We can change this number to see how the server handles the requests
      timeUnit: '1s',
    },
  },
};

export default function () {
  const res = http.get('http://staging.awesomebookstore.com/books');

  check(res, {
    'Get status is 200': (r) => res.status === 200,
    'Get Content-Type header': (r) => res.headers['Content-Type'] === 'application/json',
  });
}