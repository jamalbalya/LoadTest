import requests
import time

url = "http://example.com"  # Replace with the URL of the web server you want to test
num_requests = 10  # Replace with the number of requests you want to send
request_delay = 0.1  # Replace with the delay between requests in seconds

# Send the requests and measure the response times
response_times = []
for i in range(num_requests):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    response_times.append(response_time)
    time.sleep(request_delay)

# Calculate and print the statistics
average_response_time = sum(response_times) / len(response_times)
max_response_time = max(response_times)
min_response_time = min(response_times)
print(f"Load test results for {num_requests} requests to {url}:")
print(f"Average response time: {average_response_time:.3f}s")
print(f"Maximum response time: {max_response_time:.3f}s")
print(f"Minimum response time: {min_response_time:.3f}s")
