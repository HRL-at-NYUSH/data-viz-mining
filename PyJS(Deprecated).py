__all__ = ['example']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['finishoff', 'soundex', 'levenshtein2', 'showknownterm', 'cancelsearch', 'dictionaryiteration', 'sortscores', 'killme', 'isNumeric', 'updatePbar', 'initiatesearch', 'refresh_table', 'clean_search_term', 'spedis', 'showmoreresults', 'searchiteration', 'match', 'score_this_term', 'displayrecords', 'openinfo', 'convertnumber', 'replace_refs'])
@Js
def PyJsHoisted_spedis_(known_value, search_term, this, arguments, var=var):
    var = Scope({'known_value':known_value, 'search_term':search_term, 'this':this, 'arguments':arguments}, var)
    var.registers(['known_value', 'search_term'])
    var.put('score', Js(0.0))
    var.put('reason', Js(''))
    var.put('knwn', var.get('known_value').callprop('split', Js('')))
    var.put('srch', var.get('search_term').callprop('split', Js('')))
    var.put('pointerK', Js(0.0))
    var.put('pointerS', Js(0.0))
    var.put('end_analysis', Js(0.0))
    if (var.get('knwn').get('0')==var.get('srch').get('0')):
        var.put('pointerK', Js(1.0))
        var.put('pointerS', Js(1.0))
    else:
        if ((var.get('known_value').get('length')>Js(1.0)) and (var.get('knwn').get('0')==var.get('srch').get('1'))):
            if ((var.get('knwn').get('0')==var.get('srch').get('1')) and (var.get('knwn').get('1')==var.get('srch').get('0'))):
                var.put('pointerK', Js(2.0))
                var.put('pointerS', Js(2.0))
                var.put('score', (var.get('score')+Js(50.0)))
                var.put('reason', (var.get('reason')+Js('had to transpose first two letters<BR>')))
            else:
                var.put('pointerK', Js(1.0))
                var.put('pointerS', Js(2.0))
                var.put('score', (var.get('score')+Js(100.0)))
                var.put('reason', (var.get('reason')+Js('had to delete first letter<BR>')))
            pass
        else:
            if ((var.get('known_value').get('length')>Js(2.0)) and (var.get('knwn').get('0')==var.get('srch').get('2'))):
                if ((var.get('knwn').get('0')==var.get('srch').get('2')) and (var.get('knwn').get('1')==var.get('srch').get('1'))):
                    var.put('pointerK', Js(2.0))
                    var.put('pointerS', Js(3.0))
                    var.put('score', ((var.get('score')+Js(50.0))+Js(100.0)))
                    var.put('reason', (var.get('reason')+Js('had to delete first letter and transpose remaining two letters<BR>')))
                else:
                    var.put('pointerK', Js(1.0))
                    var.put('pointerS', Js(3.0))
                    var.put('score', ((var.get('score')+Js(100.0))+Js(50.0)))
                    var.put('reason', (var.get('reason')+Js('had to delete first two letters<BR>')))
                pass
            else:
                if ((var.get('known_value').get('length')>Js(1.0)) and (var.get('knwn').get('1')==var.get('srch').get('0'))):
                    var.put('pointerK', Js(1.0))
                    var.put('pointerS', Js(0.0))
                    var.put('score', (var.get('score')+Js(200.0)))
                    var.put('reason', (var.get('reason')+Js('had to insert the first letter<BR>')))
                else:
                    var.put('pointerK', Js(1.0))
                    var.put('pointerS', Js(1.0))
                    var.put('score', (var.get('score')+Js(200.0)))
                    var.put('reason', (var.get('reason')+Js('had to replace first letter<BR>')))
    pass
    while 1:
        if (var.get('pointerK')>=var.get('known_value').get('length')):
            var.put('score', (var.get('score')+(Js(50.0)*(var.get('search_term').get('length')-var.get('pointerS')))))
            var.put('reason', (((var.get('reason')+Js('had to truncate '))+(var.get('search_term').get('length')-var.get('pointerS')))+Js(' letters<BR>')))
            var.put('end_analysis', Js(1.0))
        else:
            if (var.get('pointerS')>=var.get('search_term').get('length')):
                var.put('score', (var.get('score')+(Js(35.0)*(var.get('known_value').get('length')-var.get('pointerK')))))
                var.put('reason', (((var.get('reason')+Js('had to append '))+(var.get('known_value').get('length')-var.get('pointerK')))+Js(' letters<BR>')))
                var.put('end_analysis', Js(1.0))
            else:
                if (var.get('knwn').get(var.get('pointerK'))==var.get('srch').get(var.get('pointerS'))):
                    (var.put('pointerK',Js(var.get('pointerK').to_number())+Js(1))-Js(1))
                    (var.put('pointerS',Js(var.get('pointerS').to_number())+Js(1))-Js(1))
                    var.put('reason', (var.get('reason')+Js('letter match<BR>')))
                else:
                    if ((var.get('search_term').get('length')>=(var.get('pointerS')+Js(1.0))) and (var.get('knwn').get(var.get('pointerK'))==var.get('srch').get((var.get('pointerS')+Js(1.0))))):
                        var.put('done', Js(0.0))
                        if (((var.get('done')==Js(0.0)) and (var.get('knwn').get((var.get('pointerK')-Js(1.0)))==var.get('srch').get(var.get('pointerS')))) and (var.get('srch').get((var.get('pointerS')-Js(1.0)))==var.get('srch').get(var.get('pointerS')))):
                            (var.put('pointerS',Js(var.get('pointerS').to_number())+Js(1))-Js(1))
                            var.put('score', (var.get('score')+Js(25.0)))
                            var.put('reason', (var.get('reason')+Js('had to delete a duplicate letter<BR>')))
                            var.put('done', Js(1.0))
                        pass
                        if (((var.get('done')==Js(0.0)) and (var.get('known_value').get('length')>=(var.get('pointerK')+Js(1.0)))) and (var.get('knwn').get((var.get('pointerK')+Js(1.0)))==var.get('srch').get(var.get('pointerS')))):
                            (var.put('pointerK',Js(var.get('pointerK').to_number())+Js(1))-Js(1))
                            (var.put('pointerS',Js(var.get('pointerS').to_number())+Js(1))-Js(1))
                            (var.put('pointerK',Js(var.get('pointerK').to_number())+Js(1))-Js(1))
                            (var.put('pointerS',Js(var.get('pointerS').to_number())+Js(1))-Js(1))
                            var.put('score', (var.get('score')+Js(50.0)))
                            var.put('reason', (var.get('reason')+Js('had to transpose two letters<BR>')))
                            var.put('done', Js(1.0))
                        pass
                        if (var.get('done')==Js(0.0)):
                            (var.put('pointerS',Js(var.get('pointerS').to_number())+Js(1))-Js(1))
                            var.put('score', (var.get('score')+Js(50.0)))
                            var.put('reason', (var.get('reason')+Js('had to delete a letter<BR>')))
                        pass
                    else:
                        if ((var.get('known_value').get('length')>=(var.get('pointerK')+Js(1.0))) and (var.get('knwn').get((var.get('pointerK')+Js(1.0)))==var.get('srch').get(var.get('pointerS')))):
                            (var.put('pointerK',Js(var.get('pointerK').to_number())+Js(1))-Js(1))
                            var.put('score', (var.get('score')+Js(100.0)))
                            var.put('reason', (var.get('reason')+Js('had to insert a letter<BR>')))
                        else:
                            if (var.get('knwn').get(var.get('pointerK'))!=var.get('srch').get(var.get('pointerS'))):
                                if ((var.get('known_value').get('length')>=(var.get('pointerK')+Js(1.0))) and (var.get('knwn').get((var.get('pointerK')+Js(1.0)))!=var.get('srch').get(var.get('pointerS')))):
                                    if ((var.get('search_term').get('length')>=(var.get('pointerS')+Js(1.0))) and (var.get('knwn').get(var.get('pointerK'))!=var.get('srch').get((var.get('pointerS')+Js(1.0))))):
                                        (var.put('pointerK',Js(var.get('pointerK').to_number())+Js(1))-Js(1))
                                        (var.put('pointerS',Js(var.get('pointerS').to_number())+Js(1))-Js(1))
                                        var.put('score', (var.get('score')+Js(100.0)))
                                        var.put('reason', (var.get('reason')+Js('had to replace a letter<BR>')))
                                    pass
                                pass
                            else:
                                var.get('alert')(Js('An error occurred while performing the Spedis calculation - please report this to james.p.harris@ons.gsi.gov.uk'))
        pass
        if not (var.get('end_analysis')!=Js(1.0)):
            break
    return (var.get('score')/var.get('known_value').get('length'))
PyJsHoisted_spedis_.func_name = 'spedis'
var.put('spedis', PyJsHoisted_spedis_)
@Js
def PyJsHoisted_levenshtein2_(str1, str2, this, arguments, var=var):
    var = Scope({'str1':str1, 'str2':str2, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'l2', 'str2', 'i', 'd', 'l1', 'str1'])
    var.put('l1', var.get('str1').get('length'))
    var.put('l2', var.get('str2').get('length'))
    if PyJsStrictEq(var.get('Math').callprop('min', var.get('l1'), var.get('l2')),Js(0.0)):
        return var.get('Math').callprop('max', var.get('l1'), var.get('l2'))
    pass
    var.put('i', Js(0.0))
    var.put('j', Js(0.0))
    var.put('d', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<=var.get('l1')):
        try:
            var.get('d').put(var.get('i'), Js([]))
            var.get('d').get(var.get('i')).put('0', var.get('i'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<=var.get('l2')):
        try:
            var.get('d').get('0').put(var.get('j'), var.get('j'))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    pass
    #for JS loop
    var.put('i', Js(1.0))
    while (var.get('i')<=var.get('l1')):
        try:
            #for JS loop
            var.put('j', Js(1.0))
            while (var.get('j')<=var.get('l2')):
                try:
                    def PyJs_LONG_0_(var=var):
                        return var.get('Math').callprop('min', (var.get('d').get((var.get('i')-Js(1.0))).get(var.get('j'))+Js(1.0)), (var.get('d').get(var.get('i')).get((var.get('j')-Js(1.0)))+Js(1.0)), (var.get('d').get((var.get('i')-Js(1.0))).get((var.get('j')-Js(1.0)))+(Js(0.0) if PyJsStrictEq(var.get('str1').callprop('charAt', (var.get('i')-Js(1.0))),var.get('str2').callprop('charAt', (var.get('j')-Js(1.0)))) else Js(1.0))))
                    var.get('d').get(var.get('i')).put(var.get('j'), PyJs_LONG_0_())
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return (Js(1.0)-(var.get('d').get(var.get('l1')).get(var.get('l2'))/var.get('Math').callprop('max', var.get('l1'), var.get('l2'))))
PyJsHoisted_levenshtein2_.func_name = 'levenshtein2'
var.put('levenshtein2', PyJsHoisted_levenshtein2_)
@Js
def PyJsHoisted_soundex_(text, this, arguments, var=var):
    var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
    var.registers(['text'])
    var.put('subtext', var.get('text').callprop('substr', Js(1.0), var.get('text').get('length')))
    var.put('subtext', var.get('subtext').callprop('replace', JsRegExp('/[aeiouhwy ]+/g'), Js('')))
    var.put('deduplicate', var.get('subtext').callprop('replace', JsRegExp('/[^\\w\\s]|(.)(?=\\1)/gi'), Js('')))
    var.put('sxcode', var.get('text').callprop('substr', Js(0.0), Js(1.0)))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('subtext').get('length')):
        try:
            while 1:
                SWITCHED = False
                CONDITION = (var.get('subtext').callprop('substr', var.get('j'), Js(1.0)))
                if True:
                    SWITCHED = True
                    var.put('score', Js(0.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('b')):
                    SWITCHED = True
                    var.put('score', Js(1.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('p')):
                    SWITCHED = True
                    var.put('score', Js(1.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('f')):
                    SWITCHED = True
                    var.put('score', Js(1.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('v')):
                    SWITCHED = True
                    var.put('score', Js(1.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('c')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('s')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('k')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('g')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('j')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('q')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('x')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('z')):
                    SWITCHED = True
                    var.put('score', Js(2.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('d')):
                    SWITCHED = True
                    var.put('score', Js(3.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('t')):
                    SWITCHED = True
                    var.put('score', Js(3.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('l')):
                    SWITCHED = True
                    var.put('score', Js(4.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('m')):
                    SWITCHED = True
                    var.put('score', Js(5.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('n')):
                    SWITCHED = True
                    var.put('score', Js(5.0))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('r')):
                    SWITCHED = True
                    var.put('score', Js(6.0))
                    break
                SWITCHED = True
                break
            pass
            var.put('sxcode', (var.get('sxcode')+var.get('score')))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    pass
    var.put('sxfinal', var.get('sxcode').callprop('replace', JsRegExp('/[^\\w\\s]|(.)(?=\\1)/gi'), Js('')))
    if (var.get('sxfinal').get('length')<Js(4.0)):
        while 1:
            var.put('sxfinal', (var.get('sxfinal')+Js('0')))
            if not (var.get('sxfinal').get('length')<Js(4.0)):
                break
    pass
    return var.get('sxfinal')
PyJsHoisted_soundex_.func_name = 'soundex'
var.put('soundex', PyJsHoisted_soundex_)
@Js
def PyJsHoisted_match_(known_value, search_term, this, arguments, var=var):
    var = Scope({'known_value':known_value, 'search_term':search_term, 'this':this, 'arguments':arguments}, var)
    var.registers(['known_value', 'search_term'])
    var.put('raw_spedis_score', Js(0.0))
    var.put('spedis_score', Js(0.0))
    var.put('lev_score', Js(1.0))
    var.put('sxscore1', Js(''))
    var.put('sxscore2', Js(''))
    var.put('sxmatch', Js(0.0))
    var.put('matchscore', Js(0.0))
    if (var.get('known_value')==var.get('search_term')):
        var.put('matchscore', Js(100.0))
    else:
        var.put('raw_spedis_score', var.get('spedis')(var.get('known_value'), var.get('search_term')))
        var.put('spedis_score', (((((-Js(0.01))*var.get('raw_spedis_score'))*var.get('raw_spedis_score'))-(Js(1.05)*var.get('raw_spedis_score')))+Js(100.0)))
        var.put('lev_score', (var.get('levenshtein2')(var.get('known_value'), var.get('search_term'))*Js(100.0)))
        var.put('sxscore1', var.get('soundex')(var.get('known_value')))
        var.put('sxscore2', var.get('soundex')(var.get('search_term')))
        if (var.get('sxscore1').callprop('charAt', Js(0.0))==var.get('sxscore2').callprop('charAt', Js(0.0))):
            var.put('sxmatch', (var.get('sxmatch')+Js(40.0)))
        pass
        if (var.get('sxscore1').callprop('charAt', Js(1.0))==var.get('sxscore2').callprop('charAt', Js(1.0))):
            var.put('sxmatch', (var.get('sxmatch')+Js(25.0)))
        pass
        if (var.get('sxscore1').callprop('charAt', Js(2.0))==var.get('sxscore2').callprop('charAt', Js(2.0))):
            var.put('sxmatch', (var.get('sxmatch')+Js(10.0)))
        pass
        if (var.get('sxscore1').callprop('charAt', Js(3.0))==var.get('sxscore2').callprop('charAt', Js(3.0))):
            if ((var.get('sxscore1').get('length')==Js(4.0)) and (var.get('sxscore2').get('length')==Js(4.0))):
                if (var.get('sxmatch')!=Js(0.0)):
                    var.put('sxmatch', (var.get('sxmatch')+Js(25.0)))
                pass
            else:
                if (var.get('sxmatch')!=Js(0.0)):
                    var.put('sxmatch', (var.get('sxmatch')+Js(10.0)))
                pass
            pass
        pass
        if (var.get('Math').callprop('min', var.get('sxscore1').get('length'), var.get('sxscore2').get('length'))>Js(4.0)):
            #for JS loop
            var.put('n', Js(4.0))
            while (var.get('n')<=(var.get('Math').callprop('min', var.get('sxscore1').get('length'), var.get('sxscore2').get('length'))-Js(1.0))):
                try:
                    if (var.get('sxscore1').callprop('charAt', var.get('n'))==var.get('sxscore2').callprop('charAt', var.get('n'))):
                        var.put('sxmatch', (var.get('sxmatch')+(Js(15.0)/(var.get('Math').callprop('max', var.get('sxscore1').get('length'), var.get('sxscore2').get('length'))-Js(4.0)))))
                    pass
                finally:
                        (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
            pass
        pass
        if ((var.get('spedis_score')<Js(20.0)) or (var.get('lev_score')<Js(45.0))):
            var.put('matchscore', Js(0.0))
        else:
            var.put('matchscore', ((((var.get('spedis_score')+var.get('lev_score'))/Js(2.0))-Js(10.0))+(Js(10.0)*(var.get('sxmatch')/Js(100.0)))))
        pass
    pass
    return var.get('matchscore')
PyJsHoisted_match_.func_name = 'match'
var.put('match', PyJsHoisted_match_)
@Js
def PyJsHoisted_refresh_table_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('document').callprop('getElementById', Js('results_table')).put('innerHTML', Js(''))
    if (var.get('document').get('pinpoint_form').get('search_term').get('value')==Js('')):
        var.get('document').callprop('getElementById', Js('results_table')).put('innerHTML', Js('Insufficient text provided in search box.'))
    else:
        var.get('document').callprop('getElementById', Js('results_table')).callprop('scrollIntoView')
        var.get('updatePbar')(Js('progressbar_srch'), Js(0.0))
        var.get('updatePbar')(Js('progressbar_mtch'), Js(0.0))
        var.get('updatePbar')(Js('progressbar_oput'), Js(0.0))
        var.get('document').callprop('getElementById', Js('img_mtch')).put('src', Js('data/pause.gif'))
        var.get('document').callprop('getElementById', Js('img_oput')).put('src', Js('data/pause.gif'))
        var.get('document').callprop('getElementById', Js('progressbarwrapper')).get('style').put('display', Js('block'))
        var.get('document').callprop('getElementById', Js('progresstitle')).put('innerHTML', Js('Please wait, searching for occupation titles:'))
        var.get('document').callprop('getElementById', Js('search_jobs')).put('disabled', Js(True))
        var.get('document').callprop('getElementById', Js('search_cancel')).put('disabled', Js(False))
        var.put('killme', Js(False))
        var.put('z', var.get('setTimeout')(Js('initiatesearch()'), Js(1.0)))
    pass
    return Js(False)
PyJsHoisted_refresh_table_.func_name = 'refresh_table'
var.put('refresh_table', PyJsHoisted_refresh_table_)
@Js
def PyJsHoisted_initiatesearch_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    var.get('document').callprop('getElementById', Js('img_srch')).put('src', Js('data/progress.gif'))
    var.put('wholedisplaytext', Js(''))
    var.put('displayed', Js(0.0))
    var.put('changes_to_text', Js(''))
    #for JS loop
    var.put('w', Js(0.0))
    while (var.get('w')<var.get('socREC').get('length')):
        try:
            var.get('socREC').get(var.get('w')).put('0', Js(0.0))
        finally:
                (var.put('w',Js(var.get('w').to_number())+Js(1))-Js(1))
    pass
    var.get('updatePbar')(Js('progressbar_srch'), Js(5.0))
    for PyJsTemp in var.get('job_dictionary'):
        var.put('i', PyJsTemp)
        var.get('job_dictionary').put(var.get('i'), Js(0.0))
    pass
    var.get('updatePbar')(Js('progressbar_srch'), Js(10.0))
    var.put('z', var.get('setTimeout')(Js('clean_search_term()'), Js(1.0)))
PyJsHoisted_initiatesearch_.func_name = 'initiatesearch'
var.put('initiatesearch', PyJsHoisted_initiatesearch_)
@Js
def PyJsHoisted_clean_search_term_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.put('search_term', var.get('document').get('pinpoint_form').get('search_term').get('value').callprop('replace', JsRegExp('/^\\s\\s*/'), Js('')).callprop('replace', JsRegExp('/\\s\\s*$/'), Js('')).callprop('toLowerCase'))
    var.get('updatePbar')(Js('progressbar_srch'), Js(15.0))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<var.get('replacementword_full_1').get('length')):
        try:
            var.put('before', var.get('search_term'))
            var.put('search_term', var.get('search_term').callprop('replace', var.get('replacementword_full_1').get(var.get('x')), var.get('replacementword_full_2').get(var.get('x'))))
            if (var.get('before')!=var.get('search_term')):
                if ((var.get('replacementword_full_2').get(var.get('x'))==Js('')) or (var.get('replacementword_full_2').get(var.get('x'))==Js(' '))):
                    var.put('changes_to_text', (((var.get('changes_to_text')+Js(", deleted term: '"))+var.get('replacementword_full_1').get(var.get('x')))+Js("'")))
                else:
                    var.put('changes_to_text', (((((var.get('changes_to_text')+Js(", replaced term: '"))+var.get('replacementword_full_1').get(var.get('x')))+Js("' with '"))+var.get('replacementword_full_2').get(var.get('x')))+Js("'")))
                pass
            pass
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    pass
    var.get('updatePbar')(Js('progressbar_srch'), Js(30.0))
    var.put('search_term', var.get('search_term').callprop('replace', JsRegExp("/[^a-z0-9' ]+/g"), Js('')))
    var.put('search_words', var.get('search_term').callprop('split', Js(' ')))
    var.get('updatePbar')(Js('progressbar_srch'), Js(35.0))
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<var.get('search_words').get('length')):
        try:
            #for JS loop
            var.put('y', Js(0.0))
            while (var.get('y')<var.get('replacementword_sngl_1').get('length')):
                try:
                    if (var.get('search_words').get(var.get('x'))==var.get('replacementword_sngl_1').get(var.get('y'))):
                        var.get('search_words').put(var.get('x'), var.get('replacementword_sngl_2').get(var.get('y')))
                        if ((var.get('replacementword_sngl_2').get(var.get('y'))==Js('')) or (var.get('replacementword_sngl_2').get(var.get('y'))==Js(' '))):
                            var.put('changes_to_text', (((var.get('changes_to_text')+Js(", deleted term: '"))+var.get('replacementword_sngl_1').get(var.get('y')))+Js("'")))
                        else:
                            var.put('changes_to_text', (((((var.get('changes_to_text')+Js(", replaced term: '"))+var.get('replacementword_sngl_1').get(var.get('y')))+Js("' with '"))+var.get('replacementword_sngl_2').get(var.get('y')))+Js("'")))
                        pass
                    pass
                finally:
                        (var.put('y',Js(var.get('y').to_number())+Js(1))-Js(1))
            pass
            if ((var.get('search_words').get(var.get('x'))==Js('')) or (var.get('search_words').get(var.get('x'))==Js(' '))):
                var.get('search_words').callprop('splice', var.get('x'), Js(1.0))
            pass
            var.get('updatePbar')(Js('progressbar_srch'), (Js(35.0)+((Js(45.0)*var.get('x'))/var.get('search_words').get('length'))))
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    pass
    #for JS loop
    var.put('x', Js(0.0))
    while (var.get('x')<var.get('search_words').get('length')):
        try:
            def PyJs_LONG_2_(var=var):
                def PyJs_LONG_1_(var=var):
                    return ((((((((var.get('search_words').get(var.get('x'))==Js(0.0)) or (var.get('search_words').get(var.get('x'))==Js(1.0))) or (var.get('search_words').get(var.get('x'))==Js(2.0))) or (var.get('search_words').get(var.get('x'))==Js(3.0))) or (var.get('search_words').get(var.get('x'))==Js(4.0))) or (var.get('search_words').get(var.get('x'))==Js(5.0))) or (var.get('search_words').get(var.get('x'))==Js(6.0))) or (var.get('search_words').get(var.get('x'))==Js(7.0)))
                return (((((((PyJs_LONG_1_() or (var.get('search_words').get(var.get('x'))==Js(8.0))) or (var.get('search_words').get(var.get('x'))==Js(9.0))) or (var.get('search_words').get(var.get('x'))==Js(10.0))) or (var.get('search_words').get(var.get('x'))==Js(11.0))) or (var.get('search_words').get(var.get('x'))==Js(12.0))) or (var.get('search_words').get(var.get('x'))==Js(13.0))) or (var.get('search_words').get(var.get('x'))==Js(14.0)))
            if ((((((PyJs_LONG_2_() or (var.get('search_words').get(var.get('x'))==Js(15.0))) or (var.get('search_words').get(var.get('x'))==Js(16.0))) or (var.get('search_words').get(var.get('x'))==Js(17.0))) or (var.get('search_words').get(var.get('x'))==Js(18.0))) or (var.get('search_words').get(var.get('x'))==Js(19.0))) or (var.get('search_words').get(var.get('x'))==Js(20.0))):
                var.put('changes_to_text', (((((var.get('changes_to_text')+Js(", replaced word: '"))+var.get('search_words').get(var.get('x')))+Js("' with '"))+var.get('convertnumber')(var.get('search_words').get(var.get('x'))))+Js("'")))
                var.get('search_words').put(var.get('x'), var.get('convertnumber')(var.get('search_words').get(var.get('x'))))
            pass
        finally:
                (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
    pass
    var.put('search_term', var.get('search_words').callprop('join', Js(' ')))
    if (var.get('search_term').callprop('replace', JsRegExp('/\\s/g'), Js(''))==Js('')):
        def PyJs_LONG_3_(var=var):
            return ((((Js('<B>You searched for: </B><FONT COLOR="blue">')+(Js('- no text -') if (var.get('search_term')==Js('')) else var.get('search_term')))+Js('</FONT>'))+(Js('') if (var.get('changes_to_text')==Js('')) else ((Js('<BR>(where the following changes were made: ')+var.get('changes_to_text').callprop('substr', Js(2.0), var.get('changes_to_text').get('length')))+Js(')'))))+Js('<BR><BR>There were <B>no results</B> to display. Perhaps you could try alternative words/terms in your search.'))
        var.get('document').callprop('getElementById', Js('results_table')).put('innerHTML', PyJs_LONG_3_())
        var.get('updatePbar')(Js('progressbar_oput'), Js(100.0))
        var.get('document').callprop('getElementById', Js('img_oput')).put('src', Js('data/done.gif'))
        var.get('document').callprop('getElementById', Js('progresstitle')).put('innerHTML', Js('Search complete!'))
        var.get('document').callprop('getElementById', Js('search_jobs')).put('disabled', Js(False))
        var.get('document').callprop('getElementById', Js('search_cancel')).put('disabled', Js(True))
        var.get('document').callprop('getElementById', Js('progressbarwrapper')).get('style').put('display', Js('none'))
    else:
        var.get('updatePbar')(Js('progressbar_srch'), Js(100.0))
        var.get('document').callprop('getElementById', Js('img_srch')).put('src', Js('data/done.gif'))
        var.get('document').callprop('getElementById', Js('img_mtch')).put('src', Js('data/progress.gif'))
        var.put('z', var.get('setTimeout')(Js('dictionaryiteration(0)'), Js(2.0)))
    pass
PyJsHoisted_clean_search_term_.func_name = 'clean_search_term'
var.put('clean_search_term', PyJsHoisted_clean_search_term_)
@Js
def PyJsHoisted_dictionaryiteration_(myval, this, arguments, var=var):
    var = Scope({'myval':myval, 'this':this, 'arguments':arguments}, var)
    var.registers(['myval', 'i'])
    if (var.get('killme')==Js(True)):
        var.get('cancelsearch')()
    else:
        for PyJsTemp in var.get('job_dictionary'):
            var.put('i', PyJsTemp)
            var.put('newscore', Js(0.0))
            var.put('newscore', var.get('match')(var.get('i'), var.get('search_words').get(var.get('myval')).callprop('replace', JsRegExp('/[-]+/g'), Js(''))))
            if (var.get('newscore')>var.get('job_dictionary').get(var.get('i'))):
                var.get('job_dictionary').put(var.get('i'), var.get('newscore'))
            pass
        pass
        var.get('updatePbar')(Js('progressbar_mtch'), ((Js(50.0)*var.get('myval'))/var.get('search_words').get('length')))
        var.put('myval', (var.get('myval')+Js(1.0)))
        if (var.get('myval')>=var.get('search_words').get('length')):
            var.put('z', var.get('setTimeout')(Js('searchiteration(0)'), Js(1.0)))
        else:
            var.put('z', var.get('setTimeout')(((Js('dictionaryiteration(')+var.get('myval'))+Js(')')), Js(2.0)))
        pass
    pass
PyJsHoisted_dictionaryiteration_.func_name = 'dictionaryiteration'
var.put('dictionaryiteration', PyJsHoisted_dictionaryiteration_)
@Js
def PyJsHoisted_searchiteration_(myval, this, arguments, var=var):
    var = Scope({'myval':myval, 'this':this, 'arguments':arguments}, var)
    var.registers(['myval'])
    if (var.get('killme')==Js(True)):
        var.get('cancelsearch')()
    else:
        if ((var.get('myval')+Js(50.0))>=var.get('socREC').get('length')):
            var.put('topval', var.get('socREC').get('length'))
        else:
            var.put('topval', (var.get('myval')+Js(51.0)))
        pass
        #for JS loop
        var.put('w', var.get('myval'))
        while (var.get('w')<var.get('topval')):
            try:
                var.get('socREC').get(var.get('w')).put('0', var.get('score_this_term')(var.get('w')))
            finally:
                    (var.put('w',Js(var.get('w').to_number())+Js(1))-Js(1))
        pass
        var.put('myval', (var.get('myval')+Js(50.0)))
        var.get('updatePbar')(Js('progressbar_mtch'), (Js(50.0)+((Js(50.0)*var.get('w'))/var.get('socREC').get('length'))))
        if (var.get('myval')>=var.get('socREC').get('length')):
            var.put('z', var.get('setTimeout')(Js('sortscores()'), Js(2.0)))
        else:
            var.put('z', var.get('setTimeout')(((Js('searchiteration(')+var.get('myval'))+Js(')')), Js(1.0)))
        pass
    pass
PyJsHoisted_searchiteration_.func_name = 'searchiteration'
var.put('searchiteration', PyJsHoisted_searchiteration_)
@Js
def PyJsHoisted_score_this_term_(w, this, arguments, var=var):
    var = Scope({'w':w, 'this':this, 'arguments':arguments}, var)
    var.registers(['w'])
    var.put('totalscore', Js(0.0))
    #for JS loop
    var.put('y', Js(3.0))
    while (var.get('y')<var.get('socREC').get(var.get('w')).get('length')):
        try:
            var.put('totalscore', (var.get('totalscore')+var.get('job_dictionary').get(var.get('socREC').get(var.get('w')).get(var.get('y')).callprop('replace', JsRegExp('/[-]+/g'), Js('')))))
        finally:
                (var.put('y',Js(var.get('y').to_number())+Js(1))-Js(1))
    pass
    return (var.get('totalscore')/(var.get('socREC').get(var.get('w')).get('length')-Js(3.0)))
PyJsHoisted_score_this_term_.func_name = 'score_this_term'
var.put('score_this_term', PyJsHoisted_score_this_term_)
@Js
def PyJsHoisted_sortscores_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('document').callprop('getElementById', Js('img_mtch')).put('src', Js('data/done.gif'))
    var.get('document').callprop('getElementById', Js('img_oput')).put('src', Js('data/progress.gif'))
    var.put('scoreranking', var.get('Array').create())
    var.put('x', Js(0.0))
    #for JS loop
    var.put('w', Js(0.0))
    while (var.get('w')<var.get('socREC').get('length')):
        try:
            if (var.get('isNumeric')(var.get('socREC').get(var.get('w')).get('0')) and (var.get('socREC').get(var.get('w')).get('0')>Js(40.0))):
                var.put('rawscore', Js(0.0))
                var.put('rawscore', var.get('Math').callprop('round', (var.get('socREC').get(var.get('w')).get('0')*(var.get('socREC').get(var.get('w')).get('length')-Js(3.0)))))
                var.put('temprawscore', var.get('rawscore').callprop('toString'))
                while 1:
                    var.put('temprawscore', (Js('0')+var.get('temprawscore')))
                    if not (var.get('temprawscore').get('length')<Js(9.0)):
                        break
                var.put('tempadjscore', Js(0.0))
                var.put('tempadjscore', var.get('Math').callprop('round', (var.get('socREC').get(var.get('w')).get('0')*Js(1000.0))))
                var.put('tempfinalscore', (var.get('tempadjscore')+var.get('temprawscore')))
                var.get('scoreranking').put((var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1)), (var.get('tempfinalscore')*Js(1.0)))
            pass
        finally:
                (var.put('w',Js(var.get('w').to_number())+Js(1))-Js(1))
    pass
    var.get('updatePbar')(Js('progressbar_oput'), Js(5.0))
    var.put('rankedscores', var.get('Array').create())
    @Js
    def PyJs_anonymous_4_(a, b, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'b'])
        return (var.get('b')-var.get('a'))
    PyJs_anonymous_4_._set_name('anonymous')
    var.put('rankedscores', var.get('scoreranking').callprop('sort', PyJs_anonymous_4_))
    var.get('updatePbar')(Js('progressbar_oput'), Js(20.0))
    var.put('w', Js(1.0))
    while 1:
        if (var.get('rankedscores').get(var.get('w'))==var.get('rankedscores').get((var.get('w')-Js(1.0)))):
            var.get('rankedscores').callprop('splice', var.get('w'), Js(1.0))
        else:
            (var.put('w',Js(var.get('w').to_number())+Js(1))-Js(1))
        pass
        if not (var.get('w')<var.get('rankedscores').get('length')):
            break
    var.get('updatePbar')(Js('progressbar_oput'), Js(35.0))
    var.put('z', var.get('setTimeout')(((Js('displayrecords(0,')+var.get('defaultnorecords'))+Js(')')), Js(1.0)))
PyJsHoisted_sortscores_.func_name = 'sortscores'
var.put('sortscores', PyJsHoisted_sortscores_)
@Js
def PyJsHoisted_displayrecords_(w, norecs, this, arguments, var=var):
    var = Scope({'w':w, 'norecs':norecs, 'this':this, 'arguments':arguments}, var)
    var.registers(['norecs', 'w'])
    if (var.get('killme')==Js(True)):
        var.get('cancelsearch')()
    else:
        if ((var.get('w')<var.get('rankedscores').get('length')) and (var.get('displayed')<var.get('norecs'))):
            #for JS loop
            var.put('x', Js(0.0))
            while (var.get('x')<var.get('socREC').get('length')):
                try:
                    var.put('rawscore', Js(0.0))
                    var.put('rawscore', var.get('Math').callprop('round', (var.get('socREC').get(var.get('x')).get('0')*(var.get('socREC').get(var.get('x')).get('length')-Js(3.0)))))
                    var.put('temprawscore', var.get('rawscore').callprop('toString'))
                    while 1:
                        var.put('temprawscore', (Js('0')+var.get('temprawscore')))
                        if not (var.get('temprawscore').get('length')<Js(9.0)):
                            break
                    var.put('tempadjscore', Js(0.0))
                    var.put('tempadjscore', var.get('Math').callprop('round', (var.get('socREC').get(var.get('x')).get('0')*Js(1000.0))))
                    var.put('tempfinalscore', (var.get('tempadjscore')+var.get('temprawscore')))
                    if (((var.get('rankedscores').get(var.get('w'))==(var.get('tempfinalscore')*Js(1.0))) and (var.get('rankedscores').get(var.get('w'))!=Js(0.0))) and (var.get('displayed')<var.get('norecs'))):
                        if (var.get('socREC').get(var.get('x')).get('2').callprop('substr', Js(0.0), Js(3.0))==Js('SE:')):
                            def PyJs_LONG_5_(var=var):
                                return (var.get('wholedisplaytext')+Js('<BR><SPAN CLASS="soc-class" onmouseover="this.style.backgroundColor=\'#D7E866\';" onmouseout="this.style.backgroundColor=\'transparent\';" onclick="z = window.open(\'data/SeeAlso.html\',\'_blank\',\'channelmode=no,directories=no,fullscreen=no,height=500,left=50,location=no,menubar=no,resizable=yes,scrollbars=yes,status=yes,titlebar=no,toolbar=no,top=50,width=700\',false);">for &#8220;'))
                            var.put('wholedisplaytext', ((((PyJs_LONG_5_()+var.get('socREC').get(var.get('x')).get('1').callprop('replace', JsRegExp('/\\s\\s*$/'), Js('')))+Js('&#8221; '))+var.get('socREC').get(var.get('x')).get('2').callprop('substr', Js(3.0), (var.get('socREC').get(var.get('x')).get('2').get('length')-Js(3.0))))+Js('</SPAN> ')))
                        else:
                            def PyJs_LONG_6_(var=var):
                                return ((((((var.get('wholedisplaytext')+Js('<BR><SPAN CLASS="soc-class" onmouseover="this.style.backgroundColor=\'#D7E866\';" onmouseout="this.style.backgroundColor=\'transparent\';" onclick="openinfo(0,'))+var.get('socREC').get(var.get('x')).get('2'))+Js(');">'))+var.get('socREC').get(var.get('x')).get('2'))+Js(', &#8220;'))+var.get('socREC').get(var.get('x')).get('1').callprop('replace', JsRegExp('/\\s\\s*$/'), Js('')))
                            var.put('wholedisplaytext', (PyJs_LONG_6_()+Js('&#8221;</SPAN> ')))
                        pass
                        (var.put('displayed',Js(var.get('displayed').to_number())+Js(1))-Js(1))
                    pass
                finally:
                        (var.put('x',Js(var.get('x').to_number())+Js(1))-Js(1))
            pass
            (var.put('w',Js(var.get('w').to_number())+Js(1))-Js(1))
            var.get('updatePbar')(Js('progressbar_oput'), (Js(35.0)+(Js(60.0)*var.get('Math').callprop('max', (var.get('w')/var.get('rankedscores').get('length')), (var.get('displayed')/var.get('norecs'))))))
            var.put('z', var.get('setTimeout')(((((Js('displayrecords(')+var.get('w'))+Js(','))+var.get('norecs'))+Js(')')), Js(1.0)))
        else:
            var.get('finishoff')(var.get('norecs'))
        pass
    pass
PyJsHoisted_displayrecords_.func_name = 'displayrecords'
var.put('displayrecords', PyJsHoisted_displayrecords_)
@Js
def PyJsHoisted_finishoff_(norecs, this, arguments, var=var):
    var = Scope({'norecs':norecs, 'this':this, 'arguments':arguments}, var)
    var.registers(['norecs'])
    if (var.get('displayed')==Js(0.0)):
        def PyJs_LONG_7_(var=var):
            return ((((Js('<B>You searched for: </B><FONT COLOR="blue">')+(Js('- no text -') if (var.get('search_term')==Js('')) else var.get('search_term')))+Js('</FONT>'))+(Js('') if (var.get('changes_to_text')==Js('')) else ((Js('<BR>(where the following changes were made: ')+var.get('changes_to_text').callprop('substr', Js(2.0), var.get('changes_to_text').get('length')))+Js(')'))))+Js('<BR><BR>There were <B>no results</B> to display. Perhaps you could try alternative words/terms in your search.'))
        var.get('document').callprop('getElementById', Js('results_table')).put('innerHTML', PyJs_LONG_7_())
    else:
        def PyJs_LONG_10_(var=var):
            def PyJs_LONG_8_(var=var):
                return ((((Js('<B>You searched for: </B><FONT COLOR="blue">')+(Js('- no text -') if (var.get('search_term')==Js('')) else var.get('search_term')))+Js('</FONT>'))+(Js('') if (var.get('changes_to_text')==Js('')) else ((Js('<BR>(where the following changes were made: ')+var.get('changes_to_text').callprop('substr', Js(2.0), var.get('changes_to_text').get('length')))+Js(')'))))+Js('<BR><BR>The <B>results of your search</B> are listed below, and are presented in reverse word order with the most likely matches first. You can click on the links for further information, and to discover your related NS-SEC code.'))
            def PyJs_LONG_9_(var=var):
                return (((((((Js('<BR><BR><FONT COLOR="darkgreen"><B>Your search returned more than ')+var.get('norecs'))+Js(' results. To display the next '))+var.get('defaultnorecords'))+Js(' results, <INPUT ID="display_more" TYPE="BUTTON" CLASS="SOCbutton" VALUE="click this button" onclick="showmoreresults('))+var.get('norecs'))+Js(');" /> or try refining your search term.</B></FONT>')) if (var.get('displayed')==var.get('norecs')) else Js(''))
            return var.get('document').callprop('getElementById', Js('results_table')).put('innerHTML', (((PyJs_LONG_8_()+var.get('wholedisplaytext'))+PyJs_LONG_9_())+Js('<BR><BR>For further information about coding, please refer to the <A HREF="http://www.ons.gov.uk/ons/guide-method/classifications/current-standard-classifications/soc2010/soc2010-volume-2-the-structure-and-index/index.html" TARGET="_blank" TITLE="Link to the SOC 2010 Volume 2 coding index">SOC 2010 Volume 2 coding index</A>.<BR>')))
        PyJs_LONG_10_()
    pass
    var.get('updatePbar')(Js('progressbar_oput'), Js(100.0))
    var.get('document').callprop('getElementById', Js('img_oput')).put('src', Js('data/done.gif'))
    var.get('document').callprop('getElementById', Js('progresstitle')).put('innerHTML', Js('Search complete!'))
    var.get('document').callprop('getElementById', Js('search_jobs')).put('disabled', Js(False))
    var.get('document').callprop('getElementById', Js('search_cancel')).put('disabled', Js(True))
    var.get('document').callprop('getElementById', Js('progressbarwrapper')).get('style').put('display', Js('none'))
PyJsHoisted_finishoff_.func_name = 'finishoff'
var.put('finishoff', PyJsHoisted_finishoff_)
@Js
def PyJsHoisted_showmoreresults_(norecs, this, arguments, var=var):
    var = Scope({'norecs':norecs, 'this':this, 'arguments':arguments}, var)
    var.registers(['norecs'])
    var.get('document').callprop('getElementById', Js('results_table')).put('innerHTML', Js(''))
    var.get('document').callprop('getElementById', Js('results_table')).callprop('scrollIntoView')
    var.put('wholedisplaytext', Js(''))
    var.put('displayed', Js(0.0))
    var.get('updatePbar')(Js('progressbar_oput'), Js(0.0))
    var.get('document').callprop('getElementById', Js('img_oput')).put('src', Js('data/progress.gif'))
    var.get('document').callprop('getElementById', Js('progresstitle')).put('innerHTML', Js('Appending more records to results...'))
    var.get('document').callprop('getElementById', Js('progressbarwrapper')).get('style').put('display', Js('block'))
    var.put('z', var.get('setTimeout')(((Js('displayrecords(0,')+(var.get('norecs')+var.get('defaultnorecords')))+Js(')')), Js(1.0)))
PyJsHoisted_showmoreresults_.func_name = 'showmoreresults'
var.put('showmoreresults', PyJsHoisted_showmoreresults_)
@Js
def PyJsHoisted_cancelsearch_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('document').callprop('getElementById', Js('search_jobs')).put('disabled', Js(False))
    var.get('document').callprop('getElementById', Js('search_cancel')).put('disabled', Js(True))
    var.get('document').callprop('getElementById', Js('img_srch')).put('src', Js('data/warning.gif'))
    var.get('document').callprop('getElementById', Js('img_mtch')).put('src', Js('data/warning.gif'))
    var.get('document').callprop('getElementById', Js('img_oput')).put('src', Js('data/warning.gif'))
    var.get('document').callprop('getElementById', Js('progresstitle')).put('innerHTML', Js('Search cancelled!'))
    var.put('killme', Js(False))
    var.get('clearTimeout')(var.get('z'))
PyJsHoisted_cancelsearch_.func_name = 'cancelsearch'
var.put('cancelsearch', PyJsHoisted_cancelsearch_)
@Js
def PyJsHoisted_convertnumber_(mynum, this, arguments, var=var):
    var = Scope({'mynum':mynum, 'this':this, 'arguments':arguments}, var)
    var.registers(['mynum'])
    return var.get('numTOtext').get(var.get('mynum'))
PyJsHoisted_convertnumber_.func_name = 'convertnumber'
var.put('convertnumber', PyJsHoisted_convertnumber_)
@Js
def PyJsHoisted_isNumeric_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    return (var.get('isNaN')(var.get('parseFloat')(var.get('x'))).neg() and var.get('isFinite')(var.get('x')))
PyJsHoisted_isNumeric_.func_name = 'isNumeric'
var.put('isNumeric', PyJsHoisted_isNumeric_)
@Js
def PyJsHoisted_updatePbar_(pbtgt, pbval, this, arguments, var=var):
    var = Scope({'pbtgt':pbtgt, 'pbval':pbval, 'this':this, 'arguments':arguments}, var)
    var.registers(['pbval', 'pbtgt'])
    @Js
    def PyJs_anonymous_11_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('$')((Js('#')+var.get('pbtgt'))).callprop('progressbar', Js({'value':var.get('pbval')}))
    PyJs_anonymous_11_._set_name('anonymous')
    var.get('$')(PyJs_anonymous_11_)
PyJsHoisted_updatePbar_.func_name = 'updatePbar'
var.put('updatePbar', PyJsHoisted_updatePbar_)
@Js
def PyJsHoisted_openinfo_(n, myvar, this, arguments, var=var):
    var = Scope({'n':n, 'myvar':myvar, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'myvar'])
    def PyJs_LONG_12_(var=var):
        return var.get('window').callprop('open', (((Js('data/') if (var.get('n')==Js(0.0)) else Js(''))+Js('SingleClass.html?soc='))+var.get('myvar')), Js('_blank'), ((Js('channelmode=no,directories=no,fullscreen=no,height=')+(Js(500.0) if (var.get('myvar')>Js(999.0)) else Js(350.0)))+Js(',left=50,location=no,menubar=no,resizable=yes,scrollbars=yes,status=yes,titlebar=no,toolbar=no,top=50,width=700')), Js(False))
    var.put('z', PyJs_LONG_12_())
PyJsHoisted_openinfo_.func_name = 'openinfo'
var.put('openinfo', PyJsHoisted_openinfo_)
@Js
def PyJsHoisted_showknownterm_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.put('start_term', var.get('document').get('pinpoint_form').get('known_term').get('value').callprop('replace', JsRegExp('/(\\r\\n|\\n|\\r)/gm'), Js('')).callprop('replace', JsRegExp('/(\\t)/gm'), Js('')))
    if (var.get('start_term').callprop('charAt', Js(0.0))==Js('0')):
        while 1:
            var.put('start_term', var.get('start_term').callprop('substr', Js(1.0), (var.get('start_term').get('length')-Js(1.0))))
            if not (var.get('start_term').callprop('charAt', Js(0.0))==Js('0')):
                break
    pass
    var.put('specificcode', var.get('start_term').callprop('replace', JsRegExp('/[^0-9]+/g'), Js('')))
    if (((var.get('start_term')==var.get('specificcode')) and (var.get('specificcode')>Js(0.0))) and (var.get('specificcode')<Js(10000.0))):
        if var.get('socDB').get(var.get('specificcode')).neg():
            var.get('alert')(Js('The code you entered was not recognised by the database. Perhaps you typed a digit incorrectly. Please try again.'))
        else:
            var.get('openinfo')(Js(0.0), var.get('specificcode'))
        pass
    else:
        var.get('alert')(Js('The SOC code you entered is not a value code - it should be a numeric code of upto four digits - please try again'))
    pass
PyJsHoisted_showknownterm_.func_name = 'showknownterm'
var.put('showknownterm', PyJsHoisted_showknownterm_)
@Js
def PyJsHoisted_replace_refs_(tempvar, this, arguments, var=var):
    var = Scope({'tempvar':tempvar, 'this':this, 'arguments':arguments}, var)
    var.registers(['tempvar'])
    var.put('endvar', var.get('tempvar'))
    while 1:
        var.put('z', var.get('tempvar').callprop('search', JsRegExp('/[0-9]/')))
        if (var.get('z')!=(-Js(1.0))):
            if (((var.get('isNumeric')(var.get('tempvar').callprop('substr', var.get('z'), Js(1.0))) and var.get('isNumeric')(var.get('tempvar').callprop('substr', (var.get('z')+Js(1.0)), Js(1.0)))) and var.get('isNumeric')(var.get('tempvar').callprop('substr', (var.get('z')+Js(2.0)), Js(1.0)))) and var.get('isNumeric')(var.get('tempvar').callprop('substr', (var.get('z')+Js(3.0)), Js(1.0)))):
                var.put('wheretoinsert', var.get('endvar').callprop('indexOf', var.get('tempvar').callprop('substr', var.get('z'), Js(4.0))))
                def PyJs_LONG_13_(var=var):
                    return ((((((var.get('endvar').callprop('substr', Js(0.0), var.get('wheretoinsert'))+Js('<SPAN CLASS="soc-class" onclick="openinfo(1,'))+var.get('tempvar').callprop('substr', var.get('z'), Js(4.0)))+Js(');">'))+var.get('tempvar').callprop('substr', var.get('z'), Js(4.0)))+Js('</SPAN>'))+var.get('endvar').callprop('substr', (var.get('wheretoinsert')+Js(4.0)), (var.get('endvar').get('length')-(var.get('wheretoinsert')+Js(4.0)))))
                var.put('endvar', PyJs_LONG_13_())
            pass
            var.put('tempvar', var.get('tempvar').callprop('substr', (var.get('z')+Js(1.0)), (var.get('tempvar').get('length')-var.get('z'))))
        pass
        if not (var.get('tempvar').callprop('search', JsRegExp('/[0-9]/'))!=(-Js(1.0))):
            break
    return var.get('endvar')
PyJsHoisted_replace_refs_.func_name = 'replace_refs'
var.put('replace_refs', PyJsHoisted_replace_refs_)
var.put('killme', Js(False))


# Add lib to the module scope
example = var.to_python()
