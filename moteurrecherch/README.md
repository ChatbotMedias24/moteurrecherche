# Search-your-Data-with-Blazing-Fast-Speed-with-Elastic-search-and-AI-with-Semantics-Search-Demo-
Search your Data with Blazing Fast Speed with Elastic search and AI with Semantics Search Demo | 


# Demo
* http://soumilbackend.ddns.net/


# Search Results
<img width="1102" alt="1" src="https://user-images.githubusercontent.com/39345855/197408819-ea8ca7ff-67b2-4969-9aa6-576bff920d77.PNG">

<img width="1095" alt="2" src="https://user-images.githubusercontent.com/39345855/197408833-13563f22-9596-45a1-85bc-4280474cc6a0.PNG">


#### Ingest code 
* http://soumilbackend.ddns.net/ingest

# Model 
* https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1
###### multi-qa-MiniLM-L6-cos-v1
* This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and was designed for semantic search. It has been trained on 215M (question, answer) pairs from diverse sources. For an introduction to semantic search, have a look at: SBERT.net - Semantic Search


##### Read More 

* Elastic Search Performance Tuning and Optimization How We Got 80X Faster Searches a Case Study
* https://www.linkedin.com/pulse/elastic-search-performance-tuning-optimization-how-we-soumil-shah/

* A Journey for Semantics Search with Elastic Search (80M) vectors Search (1.4TB)
* https://www.linkedin.com/pulse/journey-semantics-search-elastic-80m-vectors-14tb-soumil-shah/

# Ranking Query 
###### Date based ranking with Semantics Search 
```
{
  "_source": [
    "date",
    "title"
  ],
  "query": {
    "function_score": {
      "query": {
        "match_all": {}
      },
      "script_score": {
        "script": {
          "lang": "painless",
          "source": """
                            
                            double totalScore = 0.0;
                            
                            // Get Current Docuemnt Date
                            long documentDateMillis = doc['date'].value.toInstant().toEpochMilli();
                            
                            // Get Current Date Time
                            Calendar cal = Calendar.getInstance();
                            long curentDateMillis = cal.getTimeInMillis();
                            
                            // Compute the days 
                            long diff = curentDateMillis - documentDateMillis;
                            float days_ = (diff / (1000*60*60*24));
                            int days=(int)(Math.round(days_));
                            
                            // Generate the date score
                            double dateScore = Math.exp(-days/100);
                            
                             // Generate the similarityScore score
                            double similarityScore = (cosineSimilarity(params.queryVector, 'vector' ) + 1 ); 
                            
                            
                            totalScore = totalScore +dateScore;
                            totalScore = totalScore + similarityScore;
                            
                            return totalScore;
                            
                            """,
          "params": {
            "queryVector": [
              -0.022587841376662254,
              -0.017578521743416786,
              -0.04176822677254677,
              0.01949760876595974,
              0.02583909034729004,
              -0.02938505820930004,
              0.005152575671672821,
              0.03895572945475578,
              0.00030046020401641726,
              0.05515677481889725,
              -0.03426310047507286,
              -0.027109727263450623,
              0.07422863692045212,
              -0.03721475228667259,
              0.029059212654829025,
              -0.0036088319029659033,
              -0.059305205941200256,
              -0.00837564654648304,
              0.0421333834528923,
              -0.14812935888767242,
              -0.1448422223329544,
              0.04096142202615738,
              -0.007826845161616802,
              0.015531491488218307,
              0.044031109660863876,
              -0.007772982120513916,
              0.048473257571458817,
              0.015273933298885822,
              -0.027173781767487526,
              -0.00861559621989727,
              -0.030678126960992813,
              -0.01953401416540146,
              0.05064176023006439,
              0.009445483796298504,
              0.05614006146788597,
              0.05805690214037895,
              0.04690888151526451,
              -0.08842761814594269,
              -0.02325120009481907,
              -0.0018204274820163846,
              -0.012182378210127354,
              0.00015214028826449066,
              -0.014841667376458645,
              -0.08529850840568542,
              0.028471052646636963,
              0.006503417156636715,
              0.01605868898332119,
              -0.0339103601872921,
              0.05295316502451897,
              -0.04739123955368996,
              -0.029937803745269775,
              -0.03974146395921707,
              0.028296925127506256,
              -0.10972429066896439,
              0.020340492948889732,
              0.0029615832027047873,
              -0.001906159333884716,
              0.008020799607038498,
              0.002154757734388113,
              -0.10183179378509521,
              0.030055858194828033,
              -0.030728112906217575,
              0.07846829295158386,
              0.048068638890981674,
              -0.07193750888109207,
              0.07081598043441772,
              0.022687382996082306,
              0.019128059968352318,
              0.07134703546762466,
              -0.10636468231678009,
              -0.109122134745121,
              -0.07391786575317383,
              -0.075853630900383,
              0.019696280360221863,
              0.08297397941350937,
              -0.035048291087150574,
              0.08501601219177246,
              -0.002898962004110217,
              0.05563415214419365,
              -0.01198436040431261,
              -0.03429688513278961,
              -0.06181136146187782,
              -0.13377588987350464,
              0.07653731107711792,
              -0.03662950173020363,
              -0.05422460287809372,
              0.05430637672543526,
              0.09974169731140137,
              0.0586528480052948,
              0.03674133121967316,
              0.06955048441886902,
              0.033200833946466446,
              0.036015965044498444,
              -0.0035807855892926455,
              -0.06906121224164963,
              -0.013218700885772705,
              0.03009636141359806,
              0.006306761875748634,
              -0.0429161861538887,
              0.004619710613042116,
              -0.02673284523189068,
              -0.008004647679626942,
              -0.00025778383133001626,
              -0.05647057294845581,
              0.020457575097680092,
              0.08094052225351334,
              0.04019371047616005,
              0.027294157072901726,
              0.022839123383164406,
              -0.01620486192405224,
              0.018485335633158684,
              -0.040018972009420395,
              -0.010723847895860672,
              -0.03553115576505661,
              0.07011152058839798,
              0.005641744006425142,
              -0.08122024685144424,
              -0.014347990043461323,
              0.05442875251173973,
              0.10186990350484848,
              0.04653269425034523,
              0.03705348074436188,
              0.029868202283978462,
              0.004067801404744387,
              -0.018579795956611633,
              0.028069186955690384,
              -0.05536527931690216,
              3.2349924269092776e-31,
              -0.014561071060597897,
              0.011277353391051292,
              0.00700738001614809,
              -0.004022699780762196,
              0.08684706687927246,
              0.02503865770995617,
              -0.06206580996513367,
              0.02111811749637127,
              -0.05545281991362572,
              -0.05859183520078659,
              -0.06981180608272552,
              0.011147391051054,
              -0.030800843611359596,
              -0.039667509496212006,
              0.036645904183387756,
              -0.044478025287389755,
              -0.01546869333833456,
              -0.04664592072367668,
              -0.012913701124489307,
              0.09251675009727478,
              0.058873310685157776,
              -0.10093411803245544,
              -0.020643599331378937,
              0.013543566688895226,
              0.04127904027700424,
              -0.06273446977138519,
              0.02494165487587452,
              0.016547791659832,
              0.0856356993317604,
              0.024333244189620018,
              -0.022437991574406624,
              0.014501907862722874,
              0.018567761406302452,
              -0.03457591310143471,
              -0.07262904196977615,
              -0.006087571382522583,
              -0.0698651373386383,
              -0.024418791756033897,
              -0.005611723754554987,
              0.04119924455881119,
              -0.043223824352025986,
              0.07018609344959259,
              0.04659451171755791,
              -0.022437676787376404,
              -0.018723588436841965,
              0.009277807548642159,
              0.044557757675647736,
              0.052554644644260406,
              0.09529539197683334,
              0.002505569951608777,
              -0.06266755610704422,
              -0.030275827273726463,
              0.07237454503774643,
              0.09735032171010971,
              0.06636372208595276,
              -0.002421511569991708,
              0.028708675876259804,
              -0.02454289048910141,
              0.019981585443019867,
              -0.022163942456245422,
              -0.017487717792391777,
              0.02544727921485901,
              -0.005616446491330862,
              0.03489326313138008,
              -0.02911517582833767,
              -0.015037279576063156,
              0.10793161392211914,
              0.1385790854692459,
              0.0039276001043617725,
              0.02389381267130375,
              -0.06129486858844757,
              0.06458407640457153,
              0.0848311334848404,
              -0.02731519751250744,
              -0.0689033716917038,
              0.015003147535026073,
              -0.012029172852635384,
              -0.069329172372818,
              0.019938433542847633,
              0.11576425284147263,
              0.008925393223762512,
              0.049954526126384735,
              0.03798731416463852,
              -0.011535577476024628,
              -0.01041572354733944,
              -0.011051356792449951,
              0.0100361667573452,
              0.07352006435394287,
              0.025733087211847305,
              0.049195561558008194,
              -0.106786347925663,
              0.005466901697218418,
              0.016937879845499992,
              0.0038295923732221127,
              -0.07540104538202286,
              -2.0435572559702066e-33,
              -0.062937892973423,
              -0.008619861677289009,
              -0.030930375680327415,
              -0.004770365078002214,
              0.021508343517780304,
              -0.05668199434876442,
              0.06994249671697617,
              0.03785790503025055,
              0.08602721244096756,
              -0.013533294200897217,
              -0.051022160798311234,
              -0.056377917528152466,
              -0.016233336180448532,
              -0.03687981143593788,
              -0.005317778792232275,
              -0.01784021407365799,
              -0.05507895350456238,
              -0.002488114172592759,
              0.04234064370393753,
              -0.03224586695432663,
              -0.08161939680576324,
              0.03653218597173691,
              -0.06063874438405037,
              -0.0397314690053463,
              0.03873860836029053,
              -0.03908611834049225,
              -0.03434498608112335,
              -0.009441886097192764,
              -0.049354828894138336,
              -0.04463019222021103,
              0.03097403794527054,
              0.05109352245926857,
              -0.0671389102935791,
              0.04999805614352226,
              -0.05586941912770271,
              -0.024393102154135704,
              -0.01808367669582367,
              0.01117402408272028,
              0.029638294130563736,
              -0.08266492933034897,
              0.09045879542827606,
              0.0036356255877763033,
              0.03478173539042473,
              0.012018729001283646,
              -0.004532606340944767,
              0.08131135255098343,
              -0.03372151777148247,
              0.05909235030412674,
              -0.07184644788503647,
              -0.11465821415185928,
              -0.012260978110134602,
              0.021326890215277672,
              -0.0027635570149868727,
              0.027818020433187485,
              -0.009180900640785694,
              -0.03755998983979225,
              0.026657380163669586,
              0.07608863711357117,
              -0.057772889733314514,
              0.04758908972144127,
              -0.06430265307426453,
              -0.04048025235533714,
              0.09659572690725327,
              0.04999237135052681,
              -0.071077860891819,
              0.024948596954345703,
              -0.0713215246796608,
              0.04627160355448723,
              -0.03088674508035183,
              -0.03928299620747566,
              0.03715749830007553,
              -0.07479048520326614,
              -0.031827252358198166,
              -0.05328069627285004,
              -0.04932082071900368,
              0.03728533163666725,
              -0.09281329065561295,
              -0.028359074145555496,
              -0.03831212595105171,
              -0.04131612181663513,
              0.02143719047307968,
              0.05201999098062515,
              -0.00041079422226175666,
              0.07067707180976868,
              -0.048232030123472214,
              0.08884556591510773,
              -0.05114883556962013,
              0.03964744880795479,
              0.08881106972694397,
              0.08632298558950424,
              -0.07570131868124008,
              -0.06468379497528076,
              -0.02700839564204216,
              0.0123219583183527,
              -0.027022050693631172,
              -2.418480995493983e-33,
              -0.044340673834085464,
              0.017639609053730965,
              -0.02633318118751049,
              0.05100643262267113,
              -0.02640732191503048,
              0.12424961477518082,
              -0.01898871175944805,
              0.03521905466914177,
              0.05940806493163109,
              -0.03154011070728302,
              -0.020410455763339996,
              -0.09735249727964401,
              -0.07038525491952896,
              0.10763400793075562,
              0.01733064278960228,
              0.06791145354509354,
              -0.008223057724535465,
              0.1359579861164093,
              0.032490648329257965,
              -0.044996559619903564,
              0.02481752820312977,
              0.012800502590835094,
              -0.04218365252017975,
              0.038819536566734314,
              0.004798525013029575,
              -0.038805268704891205,
              -0.02647140622138977,
              0.00969654694199562,
              -0.04901698976755142,
              -0.08404546231031418,
              -0.033522166311740875,
              -0.05989335849881172,
              -0.025978652760386467,
              -0.014081505127251148,
              0.1118026077747345,
              -0.06419635564088821,
              -0.0777963250875473,
              0.021748824045062065,
              -0.03685595467686653,
              0.04680681601166725,
              -0.05080503597855568,
              0.049184203147888184,
              -0.016715364530682564,
              -0.029760977253317833,
              0.049895308911800385,
              -0.01891971006989479,
              0.02671244367957115,
              -0.008611161261796951,
              0.0537610687315464,
              0.018191523849964142,
              0.11442620307207108,
              -0.052107956260442734,
              0.02695860154926777,
              0.03963314741849899,
              0.06705959141254425,
              0.020966749638319016,
              0.05645743012428284,
              -0.08309630304574966,
              -0.020699916407465935,
              0.004649149253964424,
              0.009184452705085278,
              -0.0006152568385004997,
              0.08316443115472794,
              -0.009257793426513672
            ]
          }
        }
      }
    }
  }
}
```

## TO DO
* Add Ranker Module with TextAI Python Library 
* Add Pagination 
* facets and Aggreations for Filters 

##### Note that I exclusively work on this project on Saturdays and Sundays and that from Monday to Friday, I have a full-time job. This serves easy and fast quick POC using some pre trained machine learning model