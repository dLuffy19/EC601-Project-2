# EC601-Project-2
## Part I: Twitter API tests
### User story
A Twitter user wants to know some specific content on Twitter, he/she can use this project to filter and get the content he/she wants.
### MVP
* User can freely get, add and delete filter rules
* User can get the filtered content after applying the rules

### Authentication
For my consumer key, consumer secret, access token key, access token secret and bearer token, I export them as environment variables as follows:
```
export 'CONSUMER_KEY'='<my_consumer_key>'
```
And then I use `os` package to access them:
```python
import os
consumer_key = os.environ.get("CONSUMER_KEY")
```
### twitter_api.py
This is the main implementation file.
### twitter_api_unittest.py
This is the unit test file.

## Part II: Google NLP tests

### User story

### MVP

### Authentication
For my API key, I export it as follows:
```
export API_KEY=<my_api_key>
```
### Sentiment analysis test
I created several test document in JSON format, and then use curl to send a request to use the sentiment analysis API.
```
curl "https://language.googleapis.com/v1/documents:analyzeSentiment?key=${API_KEY}" -s -X POST -H "Content-Type: application/json" --data-binary @<test_document_file_name>
```

For `positive_doc.json`, the result is:

```
{

  "documentSentiment": {
    "magnitude": 1.9,
    "score": 0.9
  },
  "language": "en",
  "sentences": [
    {
      "text": {
        "content": "I love basketball.",
        "beginOffset": 0
      },
      "sentiment": {
        "magnitude": 0.9,
        "score": 0.9
      }
    },
    {
      "text": {
        "content": "I think everyone should play basketball.",
        "beginOffset": 19
      },
      "sentiment": {
        "magnitude": 0.9,
        "score": 0.9
      }
    }
  ]
}
```

For `negative_doc.json`, the result is:

```
{
  "documentSentiment": {
    "magnitude": 1.1,
    "score": -0.3
  },
  "language": "en",
  "sentences": [
    {
      "text": {
        "content": "I think his performance is bad.",
        "beginOffset": 0
      },
      "sentiment": {
        "magnitude": 0.9,
        "score": -0.9
      }
    },
    {
      "text": {
        "content": "However, the movie overall is pretty good.",
        "beginOffset": 32
      },
      "sentiment": {
        "magnitude": 0.1,
        "score": 0.1
      }
    }
  ]
}
```

## Unit tests for project 2
For the unit test, I used the Python built-in `unittest` module.
The unit tests are located inside the Google_NLP_test and Twitter_API_test folders.
