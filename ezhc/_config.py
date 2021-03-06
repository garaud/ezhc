
import json
from IPython.display import HTML, display




JS_LIBS_ONE = json.dumps([
    'http://code.highcharts.com/stock/highstock.js', # contains highcharts
    'https://rawgit.com/caldwell/renderjson/master/renderjson.js',
])

JS_LIBS_ONE_sep = ';'.join(map(lambda x: 'console.log("'+x+'")', json.loads(JS_LIBS_ONE)))+';'


JS_LIBS_TWO = json.dumps([
'http://code.highcharts.com/stock/highcharts-more.js',
'http://code.highcharts.com/modules/drilldown.js',
'http://code.highcharts.com/modules/exporting.js',
'http://code.highcharts.com/modules/heatmap.js',
'http://code.highcharts.com/modules/treemap.js',
])

JS_LIBS_TWO_sep = ';'.join(map(lambda x: 'console.log("'+x+'")', json.loads(JS_LIBS_TWO)))+';'


JS_LOAD = """<script>
require(%s, function() {
    require(%s, function() {
        console.log("The following js libs loaded:");
        console.log("First:");
        %s
        console.log("Then:");
        %s
    });
});
</script>""" % (JS_LIBS_ONE, JS_LIBS_TWO, JS_LIBS_ONE_sep, JS_LIBS_TWO_sep)


def load_js_libs():
	display(HTML(JS_LOAD))


JS_SAVE = [
    'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.17/require.js',
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js',
]


API_DIR = 'api'
SCRIPTS_DIR = 'scripts'

HC_OBJECT_FILE = 'hc_object.json'
HC_OPTION_FILE = 'hc_option.json'

HS_OBJECT_FILE = 'hs_object.json'
HS_OPTION_FILE = 'hs_option.json'

FULLNAME = 'fullname'
DESCRIPTION = 'description'
DEMO = 'demo'
PARAMS = 'demo'



SAMPLES_DIR = 'samples'


DF_ONE_IDX_SEVERAL_COL = 'df_one_idx_several_col.csv'
DF_ONE_IDX_SEVERAL_COL_2 = 'df_one_idx_several_col_2.csv'
DF_ONE_IDX_ONE_COL = 'df_one_idx_one_col.csv'
DF_ONE_IDX_TWO_COL = 'df_one_idx_two_col.csv'
DF_TWO_IDX_ONE_COL = 'df_two_idx_one_col.csv'
DF_SCATTER = 'df_scatter.csv'
DF_BUBBLE = 'df_bubble.csv'
DF_HEATMAP = 'df_heatmap.csv'
DF_SEVERAL_IDX_ONE_COL = 'df_several_idx_one_col.csv'

