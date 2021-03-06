
import os
import pandas as pd
import datetime as dt
import uuid
from IPython.display import HTML


from _config import JS_LIBS_ONE, JS_LIBS_TWO, JS_SAVE
from scripts import JS_JSON_PARSE




def html(options, lib='hicharts', save=False, js_preprocess=None, callback=None):

    def json_dumps(obj):
        return pd.io.json.dumps(obj)


    _opt = dict(options)


    chart_id = str(uuid.uuid4()).replace('-', '_')
    _opt['chart']['renderTo'] = chart_id


    js_init = """
    var options = %s;
    %s
    window.opt = jQuery.extend(true, {}, options);
    console.log('Highcharts/Highstock options accessible as opt');
    """ % (json_dumps(_opt), JS_JSON_PARSE) 


    if not js_preprocess:
        js_preprocess = ''


    if callback:
        callback = ', ' + callback
    else:
        callback = ''
    

    if lib=='highcharts':
        js_call = 'new Highcharts.Chart(options%s);' % (callback)
    elif lib=='highstock':
        js_call = 'new Highcharts.StockChart(options%s);' % (callback)



    html = """
    <div id="%s"></div>
    """ % (chart_id)


    js = """<script>
    require(%s, function() {
        require(%s, function() {
            %s
            %s
            %s
        });
    });
    </script>""" % (JS_LIBS_ONE, JS_LIBS_TWO, js_init, js_preprocess, js_call)
    
    if save==True:
        if not os.path.exists('saved'):
            os.makedirs('saved')
        with open(os.path.join('saved', 'plot_'+dt.datetime.now().strftime('%Y%m%d_%H%M%S')+'.html'), 'w') as f:
            contents = """
            <script src="%s"></script>
            <script src="%s"></script>
            %s
            """ % (JS_SAVE[0], JS_SAVE[1], html+js)
            f.write(contents)
    
    return html+js

    



def plot(options, lib='hicharts', save=False, js_preprocess=None, callback=None):
    contents = html(options, lib, save, js_preprocess, callback)
    return HTML(contents)

  

