import requests 
import json

urls = ['https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=58457&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId',
'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=60530&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId',
'https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentIds=57149&includes=title,logLine,episodeCount,contentId,minReleaseYear,maxReleaseYear,genres,ratingCode,studio,contentType,product,comingSoon,original,childContent,bonusMaterials,previews,free,topContentId']

data = [['playContentArray']['playContents'][0]['title'],
        ['playContentArray']['playContents'][0]['logLine'],
        ['playContentArray']['playContents'][0]['maxReleaseYear'],
        ['playContentArray']['playContents'][0]['minReleaseYear'],
        ['playContentArray']['playContents'][0]['episodeCount'],
        ['playContentArray']['playContents'][0]['genres']
        ]

for url in enumerate(urls):{
    data.append(requests.get(url))
}
print (data)  



