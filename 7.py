dict={"天津":{"办法":{"方便":{"点和":{"聚斯金德":"发吃饱饭"}}}}}
tianjin=input("----请输入地名:")
if tianjin=="天津":
    banfa=input("----请输入地名:")
    if banfa=="办法":
        fangbian=input("----请输入地名")
        if fangbian=="方便":
          dianhe=input("----请输入地名：")
          if dianhe=="点和":
            jsjd=input("----请输入地名：")
            if jsjd=="聚斯金德":
                print(dict[tianjin][banfa][fangbian][dianhe][jsjd])
