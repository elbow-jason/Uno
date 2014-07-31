from uno.base import Element, Css, Payload

class HugeFontAwesomePanel(Element):
    element_1 = Element('element_1', 'div')
    element_1.CLASS = Css('CLASS','panel panel-primary')
    element_3 = Element('element_3', 'div')
    element_3.CLASS = Css('CLASS','panel-heading')
    element_5 = Element('element_5', 'div')
    element_5.CLASS = Css('CLASS','row')
    element_7 = Element('element_7', 'div')
    element_7.CLASS = Css('CLASS','col-xs-3')
    element_9 = Element('element_9', 'i')
    element_9.CLASS = Css('CLASS','fa fa-comments fa-5x')
    element_12 = Element('element_12', 'div')
    element_12.CLASS = Css('CLASS','col-xs-9 text-right')
    element_14 = Element('element_14', 'div')
    element_14.CLASS = Css('CLASS','huge')
    element_17 = Element('element_17', 'div')
    element_23 = Element('element_23', 'a')
    element_23.href = Css('href','#')
    element_25 = Element('element_25', 'div')
    element_25.CLASS = Css('CLASS','panel-footer')
    element_27 = Element('element_27', 'span')
    element_27.CLASS = Css('CLASS','pull-left')
    element_30 = Element('element_30', 'span')
    element_30.CLASS = Css('CLASS','pull-right')
    element_31 = Element('element_31', 'i')
    element_31.CLASS = Css('CLASS','fa fa-arrow-circle-right')
    element_33 = Element('element_33', 'div')
    element_33.CLASS = Css('CLASS','clearfix')


huge_fa_panel = HugeFontAwesomePanel('huge_fa_panel', 'div')

