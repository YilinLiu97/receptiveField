net_struct = {'ISMRMNet':{'net': [[3,1,0],[3,1,0],[3,1,0],[3,1,0],[3,1,0],[3,1,0],[3,1,0],[3,1,0],[1,1,0],[1,1,0],[1,1,0]],
               'name': ['conv1','conv2','conv3','conv4','conv5','conv6','conv7','conv8','conv9','conv10','fc_conv1', '1x1x1_conv']},
              'deepmedic_baseline':{'net':[[5,1,0],[5,1,0],[5,1,0],[5,1,0],[1,1,0]],
                                    'name':['conv1','conv2','conv3','conv4','1x1x1_conv']}}

imsize = 25

def outFromIn(isz, net, layernum):
    totstride = 1
    insize = isz
    for layer in range(layernum):
        fsize, stride, pad = net[layer]
        outsize = (insize - fsize + 2*pad) / stride + 1
        insize = outsize
        totstride = totstride * stride
    return outsize, totstride

def inFromOut(net, layernum):
    RF = 1
    for layer in reversed(range(layernum)):
        fsize, stride, pad = net[layer]
        RF = ((RF -1)* stride) + fsize
    return RF

if __name__ == '__main__':
    print "layer output sizes given image = %dx%d" % (imsize, imsize)
    
    for net in net_struct.keys():
        print '************net structrue name is %s**************'% net
        for i in range(len(net_struct[net]['net'])):
            p = outFromIn(imsize,net_struct[net]['net'], i+1)
            rf = inFromOut(net_struct[net]['net'], i+1)
            print "Layer Name = %s, Output size = %3d, Stride = % 3d, RF size = %3d" % (net_struct[net]['name'][i], p[0], p[1], rf)
        
