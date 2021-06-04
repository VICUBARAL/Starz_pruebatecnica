import requests
import json  

#Listado SERIES
url = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=58457&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url1 ='https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=60530&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url2 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=57149&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url3 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=45919&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url4 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=61184&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url5 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=60083&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url6 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=45522&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url7 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=61183&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url8 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=25586&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'
url9 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=30887&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId'

data = json.loads(requests.get(url).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url1).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url2).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url3).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url4).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url5).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url6).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url7).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url8).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['maxReleaseYear'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

data = json.loads(requests.get(url9).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['minReleaseYear'])
print(data['playContentArray']['playContents'][0]['episodeCount'])
print(data['playContentArray']['playContents'][0]['genres'])

