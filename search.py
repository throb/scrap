from google_search import search
from datetime import datetime
import json

now = datetime.now()
todayDate = datetime.date(now)
todayTime = datetime.time(now)

searchTerm = 'archetype vfx pipeline download'


###############
urlList = [
    'http://www.thegnomonworkshop.com/store/product/987/',
    'http://www.amazon.com/ARCHETYPE-VFX-Breakdown-Lighting-Rendering/dp/B00AQQGWRI',
    'http://www.graphixshare.com/tutorials/269942-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst-2012.html',
    'http://www.graphixshare.com/tutorials/269865-archetype-vfx-breakdown-lighting-and-rendering-pipeline-projectfile.html',
    'http://www.youtube.com/watch?v=_hntuaNdtYs',
    'http://cgpersia.com/2012/07/the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline-24193.html',
    'http://filekoalas.com/g/gnomon+archetype+vfx+breakdown',
    'http://www.filestube.com/query.html?q=archetype+vfx+breakdown+lighting+and+rendering+pipeline+with+rob&select=All',
    'http://www.filestube.com/7bVFdJbszVOA3jrrLb8qD3',
    'http://www.filestube.com/query.html?q=archetype+vfx+breakdown+lighting+and+rendering+pipeline&select=All',
    'http://www.dl4all.com/video-tutorials/1367293-the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline.html',
    'http://files-index.com/search.php?q=g0nm0n+archetype+vfx+breakdown',
    'http://www.4shared.net/download/4KoE3x3AacD2AhRSUGvCt0',
    'http://www.cgchannel.com/tag/archetype-vfx-breakdown-lighting-and-rendering-pipeline/',
    'http://ebooksfreedownload.org/2012/07/archetype-vfx-breakdown-lighting-and-rendering-pipeline.html',
    'http://www.hhfun.com/general-information/890379-gnomon-workshop-%E2%80%93-%E2%80%98archetype%E2%80%99-vfx-breakdown-%E2%80%93-lighting-rendering-pipeline.html',
    'http://dirtywarez.com/the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline-full-free-warez-download.html',
    'http://www.vitorrent.org/ARCHETYPE+VFX+Breakdown++Lighting+and+Rendering+Pipeline+with+Rob+Nederhorst.html',
    'http://www.musicbiatch.com/music/archetype-vfx-breakdown-lighting-and-rendering-pipeline-with/',
    'http://www.kaa4.com/showthread.php?1124-Rob-Nederhorst-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline',
    'http://econo-soft14.org/ebooks/707289-the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline.html',
    'http://www.rapidshares.freshdl.com/applications/209689-gnomon-archetype-vfx-breakdown-lighting-and.html',
    'http://www.waterstones.com/waterstonesweb/products/robert+nederhorst/archetype+vfx+breakdown3a+lighting+and+rendering+pipeline+with+rob+nederhorst/9267923/',
    'http://www.ebookee.net/Rob-Nederhorst-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-2012_1936384.html',
    'http://moviebest.org/ebooks_torrent/95133-gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst.html',
    'http://www.gironic.org/tags/Pipeline/page/2/',
    'http://rapidog.com/gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst.html',
    'http://www.artff.net/search/archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst-rs',
    'http://www.gfxfind.com/tutorials/25106-the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst.html',
    'http://www.inkebook.com/399823-archetype-vfx-breakdown-lighting-and-rendering-pipeline',
    'http://www.dlfirst.com/tutorials/135341-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhors.html',
    'http://vray.info/news/article.asp?ID=536',
    'http://www.zelevent.com/tutorial/254633-gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst.html',
    'http://www.filesonicsearch.com/the+gnomon+workshop+archetype+vfx+breakdown+lighting+and+rendering+pipeline',
    'http://fileskull.com/search.php?q=gnomon+archetype+vfx+breakdown+lighting+and+rendering+pipeline+with+rob+nederhorst',
    'http://www.downloadstube.org/%252527ARCHETYPE%252527%2BVFX%2BBreakdown%2BLighting%2Band%2BRendering%2BPipeline%2Bprojectfile/Details-DDLs-77314129.html',
    'http://www.ctevideo.com/to/archetype-vfx-breakdown-lighting-and-rendering-pipeline',
    'http://rapid-search-engine.com/?s=cache:68040937:vfx',
    'http://www.sureeno.net/tutorial/40479-gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst.html',
    'http://www.serialnumberfree.net/download/Gnomon-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-with-Rob-Nederhorst-5977364.html',
    'http://www.vincedoyle.com/arv9e36/archetype-vfx-breakdown-lighting-and-rendering-pipeline-filepost',
    'http://www.vincedoyle.com/tag/archetype-vfx-background-lighting-and-rendering-pipeline-torrent',
    'http://www.top4serials.net/41675666/gnomon+archetype+vfx.html',
    'http://www.top4serials.net/41669497/gnomon+archetype+vfx.html',
    'http://filesamba.com/search.php?q=vfx+breakdown',
    'http://www.megauploaders.com/ebooks/88762-the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline.html',
    'http://www.nutdl.com/e-learning/51425-the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline-extabit-rapidgator-.html',
    'http://ebooksmio.com/software-related/139101-archetype-vfx-breakdown-lighting-and-rendering.html',
    'http://rapidshare.zoozle.net/download.php?n=the+gnomon+workshop+archetype+vfx',
    'http://downloads.egexa.com/tutorials/1108220-gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-by-rob-nederhorst-proj.html',
    'http://www.herodown.net/heroturko/the-gnomon-workshop-archetype-vfx-breakdown-bookware-torrent-download',
    'http://www.hq-scenes.com/f11/gnomon_workshop_archetype_vfx_breakdown_bookware_8_8gb-4579726.html',
    'http://warez.freethemes4site.com/the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline/',
    'http://www.angusrobertson.com.au/book/archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst-dvd-rom/36837208/',
    'http://www.3gpskull.net/videos/archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob.html',
    'http://filekoola.com/p/pipeline',
    'http://www.xfobo.com/f74/t359587.html',
    'http://www.xfobo.com/f74/t357555.html',
    'http://www.mp3-lagu.com/archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst',
    'http://www.2torial.org/forum.php?mod=viewthread&tid=648',
    'http://www.timelinedezine.com/tutorials/27265-gnomon-archetype-vfx-break.html',
    'http://www.gfxcool.co/fa/gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst',
    'http://filenewz.com/download/D951b79792f39024d/The-Gnomon-Workshop-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-Extabit-Rapidgator/',
    'http://filenewz.com/download/FC8fb7e0abd030f31/The-Gnomon-Workshop-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline/',
    'http://showdownload.org/free_ebooks/12098-.html',
    'http://www.start72.com/pt/Gnomon-ARCHETYPE-VFX-Breakdown-Lighting-And-Rendering-Pipeline-With-Rob-Nederhorst-8.16.2013/discussion.htm',
    'http://www.gfxsea.org/tag/gnomon-archetype-vfx-breakdown-bookware-source',
    'http://filespart.com/dl/pb2usp.html',
    'http://www.downloadserials.org/download/Rob-Nederhorst-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-2012--5307692.html',
    'http://www.2013zone.com/applications/209689-gnomon-archetype-vfx-breakdown-lighting-and.html',
    'http://www.tutorgigvideo.com/v/Archetype',
    'http://www.verytorrent.com/elearning/9645-the-gnomon-workshop-archetype-vfx-breakdown-bookware-lz0.html',
    'http://downdlz.com/tutorials/1409-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst-torrent.html',
    'http://ebookcrop.com/p/4/pipeline/',
    'http://bestwebsitesdesigning.com/tutorials/2643849-the-gnomon-workshop-archetype-vfx-breakdown-lighting-and-rendering-pipeline.html',
    'http://getfilenow.com/s/archetype',
    'http://find.wiki.gov.cn/w_VFX+Pipeline/',
    'http://www.todaytorrents.com/download/Gnomon-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-with-Rob-Nederhorst-5977364.html',
    'http://rapidlibrary.com/files/nederhorst-mp3_ulzwrbcwwri89on.html',
    'http://www.downwant.com/g/gnomon-archetype-vfx-breakdown-lighting-and-rendering-pipeline-with-rob-nederhorst.html',
    'http://opendown.net/download-other/439839-gnomon-archetype-vfx-breakdown.html',
    'http://files4dl.com/search.php?q=digital+lighting+and+rendering+2nd',
    'http://www.gfxsolo.org/so/the-gnomon-workshop-archetype-vfx-breakdown-bookware-iso-lz0',
    'http://www.kugraphic.org/tags/Archetype/',
    'http://www.metacafe.com/videos_about/vfx/page-11/',
    'http://freemp3x.org/archetype-by-aaron-sims-rus-mp3-download.html',
    'http://scriptwarez.net/page/64278-g0nm0n-archetype-vfx-breakdown.html',
    'http://ns22.mainstoreonline.com/index.php?target=desc&progid=73213',
    'http://www.zxland.com/free/archetype-lighting-nzb.html',
    'http://www.allyoushare.com/128587-gnomon-archetype-vfx-breakdown-lighting-and.html',
    'http://www.nonvule.net/tags/Pipeline/page/3/',
    'http://www.freetorrentdownloads.org/download/Rob-Nederhorst-ARCHETYPE-VFX-Breakdown-Lighting-and-Rendering-Pipeline-2012--5307692.html',
    'http://www.weluminousbeings.com/doc/Cameron%20L%20Ward%20Resume.pdf',
    'http://mp3truck.com/nuke-breakdowns-showreel-mp3-download.html',
    'http://www.mafia-bb.com/324124-the-gnomon-workshop-archetype-vfx-breakdown.html',
    'http://www.tactools.ru/g0nm0n-archetype-vfx-breakdown/',
    'http://ru.rapidmore.com/download_z2vzqr',
    'http://www.youcandl.com/getlink/gnomon-archetype-vfx-breakdown-wupload',
    'http://friendfeed.com/torrent3/43b38167/gnomon-workshop-archetype-vfx-breakdown',
    'http://www.dolphindl.com/stock-images/33333-3d-pipeline-photo.html'
]

###############


#urlList = []

#for url in search (searchTerm,stop=100):
    #urlList.append(url)

accetableSites = [
    'amazon.com',
    'thegnomonworkshop.com',
    'cgchannel.com',
    'vray.info',
    'thefoundry.co.uk',
    'youtube.com',
    'vimeo.com'
    ]

outData = [
    {'searchterm':searchTerm}
    #{'date':todayDate},
    #{'time':todayTime}
    ]

for url in urlList:
    foundIllegalSite = False
    for goodSite in accetableSites:
        if goodSite.lower() in url.lower():
            break
    else:
        outData.append({'url':url})

foo = json.dumps(outData)
fh = open ('results.json','w')
for line in outData:
    fh.write(foo)
fh.close()
    