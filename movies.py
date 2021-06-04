import requests
import json

#ListadoMovies
url   = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=63740&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url1  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=62067&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url2  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=51880&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url3  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=35511&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url4  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=50752&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url5  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=63736&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url6  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=59244&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url7  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=58718&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url8  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=51827&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url9  = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=51152&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url10 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=49088&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url11 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=51917&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url12 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=51449&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url13 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=51754&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url14 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=46437&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url15 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=29285&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url16 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=38001&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'
url17 = 'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=58728&includes=title,logLine,runtime,ratingCode,mediaId,free,studio,product,contentId,audioType,releaseYear,newContent,comingSoon,images,genres,contentType,product,startDate,bonusMaterials,previews,credits'

data = json.loads(requests.get(url).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url1).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url2).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url3).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url4).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url5).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url6).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url7).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url8).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url9).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url10).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url11).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url12).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url13).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url14).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url15).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url16).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])

data = json.loads(requests.get(url17).text)
print(data['playContentArray']['playContents'][0]['title'])
print(data['playContentArray']['playContents'][0]['logLine'])
print(data['playContentArray']['playContents'][0]['releaseYear'])
print(data['playContentArray']['playContents'][0]['runtime'])
print(data['playContentArray']['playContents'][0]['genres'])
print(data['playContentArray']['playContents'][0]['credits'])