import numpy as np
# to better visulaize image, use gamma correction to transfer image real to image view
def img_real2view(img):
    gamma_correction=lambda x:np.power(x,1.0/2.2)
    img_shape=img.shape
    # gray image
    if np.size(img_shape)==2:
        # uint8
        if np.max(img)>1:
            temp_view=np.zeros_like(img,dtype=np.float32)
            temp_view=np.float32(img)/255.0 # float32, 1.0
            temp_view=gamma_correction(temp_view)
            temp_view2=np.zeros_like(img,dtype=np.uint8)
            temp_view2=np.uint8(temp_view*255)
            return temp_view2
        # float
        if np.max(img)<2:
            return gamma_correction(img)
            
    # color image
    if np.size(img_shape)==3:
        # uint8, BGR
        if np.max(img)>1:
            temp_view=np.zeros_like(img,dtype=np.float32)
            temp_view=np.float32(img[...,::-1])/255.0 # gb,1.0
            temp_view[...,-1]=gamma_correction(temp_view[...,-1])
            temp_view[...,1]=gamma_correction(temp_view[...,1])
            temp_view2=np.zeros_like(img,dtype=np.uint8)
            temp_view2=np.uint8(temp_view[...,::-1]*255) # bgr,255
            return temp_view2
        # float, RGB
        if np.max(img)<2:
            return gamma_correction(img)

def read_movie_from_h5(filename):
    h5f = h5py.File(filename,'r')
    movie_bgr_h5=h5f['movie_bgr_real'][:]
    h5f.close()
    return movie_bgr_h5
