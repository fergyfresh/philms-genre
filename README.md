# philms-genre

## How to use

Install with egg until its hosted on pypi.
```
pip install -e git+ssh://git@github.com/fergyfresh/philms-genre@master#egg=philms_genre
```

Test it out after you've installed it.

```
from philms_genre import philms_genre
print(philms_genre.scrape_top_movies())
```

*FYI this is a throttle API call at IMDb so it will take ~3-5 minutes to finish.
