Blockly.Python.python_opencv_imread = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var v = this.getFieldValue('V')
    var url = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='cv2.imread('+url+','+v+')'
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_imshow = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var name = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var img = Blockly.Python.valueToCode(this,'IMG',Blockly.Python.ORDER_ASSIGNMENT);
    var code='cv2.imshow('+name+','+img+')\n'
    return code;
}

Blockly.Python.python_opencv_waitKey = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var time=Blockly.Python.valueToCode(this,'TIME',Blockly.Python.ORDER_ASSIGNMENT);
    var code='cv2.waitKey('+time+')'
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_imwrite = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var url = Blockly.Python.valueToCode(this,'URL',Blockly.Python.ORDER_ASSIGNMENT);
    var code='cv2.imwrite('+url+','+img+')\n'
    return code;
}

Blockly.Python.python_opencv_roi = function(a) {
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var x = Blockly.Python.valueToCode(this,'X',Blockly.Python.ORDER_ASSIGNMENT);
    var y = Blockly.Python.valueToCode(this,'Y',Blockly.Python.ORDER_ASSIGNMENT);
    var w = Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h = Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var xx=Number(x)+Number(w)
    var yy=Number(y)+Number(h)
    var s = '['+y+':'+yy+','+x+':'+xx+']'
    var code=img+s
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_shape = function(a) {
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var v = this.getFieldValue('V')
    var code=img+'.shape['+v+']'
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_resize = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var v = Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var code = 'cv2.resize('+img+',('+v+','+v+'))';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_rotating = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var v = this.getFieldValue('NUM')
    if(v==90){
        var s='cv2.ROTATE_90_CLOCKWISE'
    }
    else if(v==180){
        var s='cv2.ROTATE_180'
    }
    else if(v==270){
        var s='cv2.ROTATE_90_COUNTERCLOCKWISE'
    }
    var code = 'cv2.rotate('+img+','+s+')';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_color_block= function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    Blockly.Python.definitions_['Mxopencv'] = 'from Mx import mxopencv';
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var color = Blockly.Python.valueToCode(this,'COLOR',Blockly.Python.ORDER_ASSIGNMENT);
    var code = 'mxopencv.color_block('+img+','+color+')';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_opencam = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var id = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var api = this.getFieldValue('API')
    var code = 'cv2.VideoCapture('+id+','+api+')';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_rectangle=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    Blockly.Python.definitions_['Mxopencv'] = 'from Mx import mxopencv';
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var rect = Blockly.Python.valueToCode(this,'RECT',Blockly.Python.ORDER_ASSIGNMENT);
    var color = this.getFieldValue('COLOR')
    var size = this.getFieldValue('SIZE')
    var code = 'mxopencv.rectangle('+img+','+rect+',"'+color+'",'+size+')\n'
    return code;
}

Blockly.Python.python_opencv_readcam = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var name = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code = name+'.read()[1]';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_circle=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    Blockly.Python.definitions_['Mxopencv'] = 'from Mx import mxopencv';
    var img = Blockly.Python.valueToCode(this,'IMG',Blockly.Python.ORDER_ASSIGNMENT);
    var xy = Blockly.Python.valueToCode(this,'XY',Blockly.Python.ORDER_ASSIGNMENT);
    var rad = Blockly.Python.valueToCode(this,'RAD',Blockly.Python.ORDER_ASSIGNMENT);
    var color = this.getFieldValue('COLOR')
    var tk = this.getFieldValue('TK')
    var code = 'mxopencv.circle('+img+','+xy+','+rad+',"'+color+'",'+tk+')\n'
    return code;
}

Blockly.Python.python_opencv_line=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    Blockly.Python.definitions_['Mxopencv'] = 'from Mx import mxopencv';
    var img = Blockly.Python.valueToCode(this,'IMG',Blockly.Python.ORDER_ASSIGNMENT);
    var stxy = Blockly.Python.valueToCode(this,'STXY',Blockly.Python.ORDER_ASSIGNMENT);
    var endxy = Blockly.Python.valueToCode(this,'ENDXY',Blockly.Python.ORDER_ASSIGNMENT);
    var color = this.getFieldValue('COLOR')
    var size = Blockly.Python.valueToCode(this,'SIZE',Blockly.Python.ORDER_ASSIGNMENT);
    var code = 'mxopencv.line('+img+','+stxy+','+endxy+',"'+color+'",'+size+')\n'
    return code;
}

Blockly.Python.opencv_find_camid=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    Blockly.Python.definitions_['Mxopencv'] = 'from Mx import mxopencv';
    var code = 'mxopencv.find_camid()\n'
    return code;
}

Blockly.Python.python_opencv_text=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    Blockly.Python.definitions_['Mxopencv'] = 'from Mx import mxopencv';
    var img = Blockly.Python.valueToCode(this,'IMG',Blockly.Python.ORDER_ASSIGNMENT);
    var text = Blockly.Python.valueToCode(this,'TEXT',Blockly.Python.ORDER_ASSIGNMENT);
    var xy = Blockly.Python.valueToCode(this,'XY',Blockly.Python.ORDER_ASSIGNMENT);
    var font_size = Blockly.Python.valueToCode(this,'FONTS',Blockly.Python.ORDER_ASSIGNMENT);
    var color = this.getFieldValue('COLOR')
    var size = Blockly.Python.valueToCode(this,'SIZE',Blockly.Python.ORDER_ASSIGNMENT);
    var code = 'mxopencv.text('+img+','+text+','+xy+','+font_size+',"'+color+'",'+size+')\n'
    return code;
}

Blockly.Python.python_opencv_cap_setHW=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var cap = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var w = Blockly.Python.valueToCode(this,'W',Blockly.Python.ORDER_ASSIGNMENT);
    var h = Blockly.Python.valueToCode(this,'H',Blockly.Python.ORDER_ASSIGNMENT);
    var code = cap+".set(cv2.CAP_PROP_FRAME_WIDTH, "+w+")\n"+
               cap+".set(cv2.CAP_PROP_FRAME_HEIGHT, "+h+")\n"
    return code;
}

Blockly.Python.python_opencv_FULLSCREEN=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var name = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code = "cv2.namedWindow("+name+",cv2.WND_PROP_FULLSCREEN)\n"+
                "cv2.setWindowProperty("+name+", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)\n"
    return code;
}

Blockly.Python.python_opencv_opencam_rtsp = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var id = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code = 'cv2.VideoCapture('+id+')';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_selectROI = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var t = Blockly.Python.valueToCode(this,'T',Blockly.Python.ORDER_ASSIGNMENT);
    var img = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var code = 'cv2.selectROI("'+t+'", '+img+', showCrosshair=False, fromCenter=False)';
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_tracker_cj = function(a) {
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var name = this.getFieldValue('NAME')
    var code = name;
    return [code,Blockly.Python.ORDER_ATOMIC];
}

Blockly.Python.python_opencv_tracker_init=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var name = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var img = Blockly.Python.valueToCode(this,'IMG',Blockly.Python.ORDER_ASSIGNMENT);
    var roi = Blockly.Python.valueToCode(this,'ROI',Blockly.Python.ORDER_ASSIGNMENT);
    var code = name+'.init('+img+', '+roi+')\n'
    return code;
}

Blockly.Python.python_opencv_tracker_update=function(a){
    Blockly.Python.definitions_['Opencv'] = 'import cv2';
    var name = Blockly.Python.valueToCode(this,'NAME',Blockly.Python.ORDER_ASSIGNMENT);
    var img = Blockly.Python.valueToCode(this,'IMG',Blockly.Python.ORDER_ASSIGNMENT);
    var zt = this.getFieldValue('ZT')
    var code = name+'.update('+img+')['+zt+']'
    return [code,Blockly.Python.ORDER_ATOMIC];
}
