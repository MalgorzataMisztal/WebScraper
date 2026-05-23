# WebScraper

## Project implementation steps

### Stages 1-3

1. Provide url of the product's opinions page
2. Send request to provided url
3. Fetch product name
4. Fetch all opinions from the webpage
5. Parse opinions to extract required data
6. Check if there is a next page with opinions
7. Repeat steps from 4 to 6 for all pages with opinions about product
8. Save aquired opinions

## Project inputs

### Products codes

-174130671
-186933309
-180826505
-141797721
-90558892
-39562616
### Opinion Structure
|component|name|selector|
|---------|----|--------|
|opinion ID|opinions_ID|[data-entry-id]|
|opinion’s author|author|span.user-post__author-name|
|author’s recommendation|recommendation|span.user-post__author-recomendation > em|
|score expressed in number of stars|score|span.user-post__score-count|
|opinion’s content|contact|div.user-post__text|
|list of product advantages|pros|div.review-feature__item--positive|
|list of product disadvantages|cons|div.review-feature__item--negative|
|how many users think that opinion was helpful|helpful|button.vote-yes[data-total-vote]|
|how many users think that opinion was unhelpful|unhelpful|button.vote-no[data-total-vote]|
|publishing date|publishing_date|span.user-post__published > time:nth-child(1)[datetime]|
|purchase date|purchase_date|span.user-post__published > time:nth-child(2)[datetime]|