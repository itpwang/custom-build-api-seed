Apache Benchmark
===============================================================


##1. 100 requests. 10 concurrent.

```ab -n 100 -c 10 http://127.0.0.1:5000/QuotesPorn/ > apachebenchresults.md```

####Comments on test:
Treating this as initial default test. Pretty large range of min/max connection times (almost 4x). Looking at the distribution table of Percentage of requests 
served within a certain time, we see that there is a jump in number of requests from ~80%->90%. 80% of the requests were served under 4 seconds. 
This is more likely due to the machine I am running on, a virtual cloud machine hosted by c9.io. This free development cloud is most likely run with minimal resources and thus
will not perform as well as a physical machine. However, we can still use it to test the integrity of our api at lower levels.

####Benchmark Data

This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done

Data type | benchmark result           
---|----
Server Software:    |    Werkzeug/0.9.6
Server Hostname:    |    127.0.0.1
Server Port:      |      5000
Document Path:     |     /QuotesPorn/
Document Length:    |    48912 bytes
Concurrency Level:  |    10
Time taken for tests: |  39.039 seconds
Complete requests:    |  100
Failed requests:     |   0
Total transferred:   |   4906000 bytes
HTML transferred:    |   4891200 bytes
Requests per second:  |  2.56 [#/sec] (mean)
Time per request:    |   3903.866 [ms] (mean)
Time per request:   |    390.387 [ms] (mean, across all concurrent requests)
Transfer rate:      |    122.72 [Kbytes/sec] received

####Connection Times (ms)
|        _   | min | mean |[+/-]sd|median| max |
|------------|-----|------|-------|------|-------|
| Connect    |  0  |   0  |  0.2  |   0  |    1  |
| Processing | 2946 | 3748 | 1188.7 | 3423 |  8659 |
| Waiting    | 2946 | 3748 | 1188.8 | 3418 |  8658 |
| Total      | 2946 | 3748 | 1188.8 | 3423 |  8659 |


####Percentage of the requests served within a certain time (ms)

% | requests
----|----
  50%   |3423 
  66%   |3496 
  75%   |3560 
  80%   |3615 
  90%   |5627
  95%   |7298 
  98%   |8325 
  99%   |8659 
 100%   |8659 (longest request) 
 

##2. 100 requests, 1 concurrent.

```ab -n 100 -c 1 http://127.0.0.1:5000/QuotesPorn/ >> apachebenchresults.md```

####Comments on test:
Lowering the concurrency to minimize problems caused by machine limitations. Seems more consistent looking at the resultant data. Max is 3x of min, seems like
as we increase the magnitude of concurrency, the total difference between max/min request times also widens (on that magnitude). Machine seems to perform well at lower levels.

####Benchmark Data

This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)

Data type | benchmark result
---|----
Server Software:    |    Werkzeug/0.9.6
Server Hostname:    |    127.0.0.1
Server Port:        |    5000
Document Path:      |    /QuotesPorn/
Document Length:    |    48912 bytes
Concurrency Level:  |    1
Time taken for tests: |  34.626 seconds
Complete requests:   |   100
Failed requests:     |   0
Total transferred:   |   4906000 bytes
HTML transferred:    |   4891200 bytes
Requests per second: |   2.89 [#/sec] (mean)
Time per request:     |  346.260 [ms] (mean)
Time per request:    |   346.260 [ms] (mean, across all concurrent requests)
Transfer rate:      |    138.36 [Kbytes/sec] received


####Connection Times (ms)


   _  |  min | mean | [+/-sd] | median |  max
------------|------|-----|-------|--------|-----|---|
Connect:    |    0  |  0 |  0.3   |   0   |    3
Processing: |  222 | 346 | 93.0  | 331  |   607
Waiting:   |   221 | 345 | 92.6  |  330  |   606
Total:     |   222 | 346 | 93.0  |  331  |   607

####Percentage of the requests served within a certain time (ms)

% | requests
----|----
  50%  |  331
  66%  |  363
  75%  |  411
  80%  |  427
  90%  |  469
  95%  |  563
  98%  |  580
  99%  |  607
 100%  |  607 (longest request)
 
 
##3. 1000 request. 10 concurrent.
 
```ab -n 1 -c 1 127.0.0.1:5000/politics/```

####Comments on test:
Raised number of requests to 1000, and 10 concurrent. Not expecting too much out of this one, just testing how bad it can get and if too many requests will kill it.
Some portions of test were as predicted, whereas others were not. Difference between min/max increased to 10x, which asserts our hypothesis that as #of requests go up,
the difference increases exponentially. However, the connection times of 50% and 100% requests rose gradually, which either means the machine's performance is better over 
larger amounts of requests (consistent) or there big jump in performance after a certain amount of requests (< 50%). I believe it's a combination of both, though the former
prediction needs to be tested more. End of testing on this machine.

####Benchmark Data

This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done

Data type | benchmark result
-------|-----------
Server Software:   |     Werkzeug/0.9.6
Server Hostname:    |    127.0.0.1
Server Port:       |     5000
Document Path:     |     /QuotesPorn/
Document Length:    |    48912 bytes
Concurrency Level:   |   10
Time taken for tests: |  336.238 seconds
Complete requests:   |   1000
Failed requests:    |    0
Total transferred:  |    49060000 bytes
HTML transferred:   |    48912000 bytes
Requests per second: |   2.97 [#/sec] (mean)
Time per request:   |    3362.377 [ms] (mean)
Time per request:   |    336.238 [ms] (mean, across all concurrent requests)
Transfer rate:      |    142.49 [Kbytes/sec] received

####Connection Times (ms)


       _      | min | mean | [+/-sd]  | median  | max
------------|------|-----|-------|--------|-----|---|
Connect:    |    0  |  0  | 0.2   |   0   |    4
Processing:  | 377 | 3346 | 279.2 |  3341 |   4240
Waiting:     | 377 | 3344 | 279.4 |  3340  |  4240
Total:      | 379 | 3346 | 279.1 |  3341  |  4241

####Percentage of the requests served within a certain time (ms)

% | requests
----|----
  50%  | 3341
  66%  | 3420
  75%  | 3491
  80%  | 3540
  90%  | 3650
  95%  | 3740
  98%  | 3848
  99%  | 3947
 100%  | 4241 (longest request)


