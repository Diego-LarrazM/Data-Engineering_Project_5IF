# Project 1: Movies

## DBs
- [IMDB](https://www.imdb.com/title/tt4034228/?ref_=nv_sr_srsg_0_tt_5_nm_3_in_0_q_manchester) : (all info, score, director, producer, **keywords about script**, **genre**, EVEN QUOTES!) ... https://developer.imdb.com
- [SiplyScripts](https://www.simplyscripts.com/#80) : film scripts in case we want NLP, we'd have to parse pdf->text.

(In case we go for videogames)
- [IGDB](https://www.igdb.com) : same as IMDB but for games

## Steps

1. Clean it and store it in a db for querying
- 2 (A)
    - (A) POSSIBILITY: Grafa dashboarding for film stats
- 2 (B) 
    - Cloud integration (i've already done it so not that difficult)
- 2 (C)
    - (C) Data cleaning, parsing, vectorization and reccomendation engine creation from groups(directors and actors, genre and keyworks, ...). <br><br>NULL data can be either eliminated or induced from other data (if follows a model) or LLM/NLP on scripts for keyword gen/extraction but i don't think that will be necessary except for videogames. <br><br>
    We would check for most common keywords and least common (and thus those with the msot information) to select what to use to compare.
    https://www.kaggle.com/code/fabiendaniel/film-recommendation-engine


<br>

Some of them can be done together:
- **(A and B)** having a cloud stateless grafana machine on the cloud.
- **(B and C)**  cloud stored and queried for reccomendation engine
- **(A and C)**  We could do both of course!


**REMEMBER** This is a dataeng project, it cares more for transformation, loading and storage than ML, thus B is quite valuable comapred to the otehrs in points i believe (plus it helps with performance checking with its built-in tools)


## Other Ideas

- Market shares for prediction using LSTMs (long short term memory Neural netwokors)

- [Public APIS](https://github.com/public-apis/public-apis?tab=readme-ov-file)

