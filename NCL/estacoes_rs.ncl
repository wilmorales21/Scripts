;Este código foi escrito com a ajuda do meteorologista Eliton Figueiredo(CPPMet-Pelotas)

load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin

 arq = asciiread("estacoes_rs.txt",-1,"string")

 lat = stringtofloat(str_get_field(arq,1,","))
 lat2 = stringtofloat(str_get_field(arq,1,","))
 lat3 = stringtofloat(str_get_field(arq,1," "))
;Este comando vai deslocar o texto(informações de orvalho) em 0.15 graus de latitude para baixo(-) do marcador no mapa.
 lat3 = lat3 - 0.15

 lon = stringtofloat(str_get_field(arq,2,","))
 lon2 = stringtofloat(str_get_field(arq,2,","))
;Este comando vai deslocar o texto(informações de temperatura) em 0.15 graus de longitude para esquerda(-) do marcador no mapa.
 lon2 = lon2 - 0.15
;Este comando vai deslocar o texto(informações de precipitação) em 0.39 graus de longitude para direita(+) do marcador no mapa.
 lon3 = lon2 + 0.39

 temp = str_get_field(arq,6,",")
 temp@_FillValue = -999.9          ; sets _FillValue to -999
 temp@_FillValue = ","
 delete(temp@_FillValue)

 td = str_get_field(arq,12,",")
 temp@_FillValue = -999.9          ; sets _FillValue to -999
 temp@_FillValue = ","
 delete(temp@_FillValue)

 prec = str_get_field(arq,21,",")
 temp@_FillValue = -999.9         ; sets _FillValue to -999  
 temp@_FillValue = ","
 delete(temp@_FillValue)
 
 wdir = stringtofloat(str_get_field(arq,18,","))
 wdir@_FillValue = -999.9           ; sets _FillValue to -999
 
 wspd = stringtofloat(str_get_field(arq,17,","))
 wspd@_FillValue = -999.9          ; sets _FillValue to -999
 
; Wind_component é uma função disponível na versão 6.3 do NCL
 uv = wind_component(wspd,wdir,0)
 u  = uv(0,:)
 v  = uv(1,:)

 wks = gsn_open_wks("png", "automaticas_rs.png")

  res                             = True
  res@gsnMaximize                 = True      ; maximize plot in farme
  res@gsnFrame                    = False     ; Não avança o quadro
  res@gsnDraw                     = True      ; Desenha o mapa
  res@pmTickMarkDisplayMode       = "Always"
  res@mpLimitMode                 = "LatLon"  ; Zoom no Brasil
  res@mpMinLatF                   = -34
  res@mpMaxLatF                   = -27
  res@mpMinLonF                   = -58
  res@mpMaxLonF                   = -49
  res@mpFillOn                    = False

;Código para plotar cedilha, til e acento agudo no NCL
  cedil = "c~H-13F35~K~FH2~"
  otilde = "o~H-13V2F35~D~FV-2H3~" 
  aacute = "a~H-13V2F35~B~FV-2H3~"
  agrave = "a~H-13V2F35~A~FV-2H3~"

;Título do mapa
res@gsnCenterString  = "~Z80~Temperatura, orvalho e barbelas de vento ~C~     nas esta"+cedil+otilde+"es autom"+aacute+"ticas do INMET ~C~              "+agrave+"s 06UTC de 03/04/2020"

;mapa
  res@pmTickMarkDisplayMode       = "Always"
  res@mpDataSetName               = "Earth..4"
  res@mpOutlineOn                 = True
  res@mpDataBaseVersion           = "MediumRes" 
  res@mpOutlineBoundarySets       = "AllBoundaries"
  res@mpOutlineSpecifiers         = (/"Brazil:states"/)
  res@mpFillAreaSpecifiers        = (/"Land", "Brazil:Rio Grande do Sul"/)
  res@mpSpecifiedFillColors       = (/0,-1,0/)

  gsn_define_colormap(wks,"default")

  res@gsnPaperOrientation = "portrait"
  res@mpNationalLineColor    = "8"
  res@mpGeophysicalLineColor = "8"
; res@mpProvincialLineColor = "8"

  map = gsn_csm_map(wks,res)      ; Cria o mapa do Brasil
 
;----------------------- VENTO ---------------------------------
  wmsetp("col",1) 
  wmsetp("wbs", .05)       ; Aumenta o tamanho das barbelas.
  wmbarbmap(wks, lat, lon,  u, v)
 
;----------------------- OVERLAY------------------------------

  res@tfDoNDCOverlay = True
;-------------------------------------------------------------
;Anexa texto ao mapa(plota informações de temperatura)
  txres               = True
  txres@txFontHeightF = 0.013
  txres@txJust        = "CenterRight"
  txres@txFontColor   = "Red"
  txdum = gsn_add_text(wks,map,temp,lon2,lat2,txres)  
 delete(txres)

;Anexa texto ao mapa(plota informações de temperatura do ponto de orvalho) 
  txres               = True
  txres@txFontHeightF = 0.013
  txres@txJust        = "CenterRight"
  txres@txFontColor   = "darkgreen"
  txdum = gsn_add_text(wks,map,td,lon2,lat3,txres) 

;Anexa texto ao mapa(plota informações de precipitação) 
;  txres               = True
;  txres@txFontHeightF = 0.013
;  txres@txJust        = "CenterCenter"
;  txres@txFontColor   = "Blue"
;  txdum = gsn_add_text(wks,map,prec,lon3,lat,txres) 

;Anexa marcadores ao mapa(plota o ponto de latitude e longitude das estações)
  mkres               = True
  mkres@gsMarkerIndex = 16
  mkres@gsMarkerSizeF = 8
  mkres@gsMarkerColor = "black"
  mkdum = gsn_add_polymarker(wks,map,lon,lat,mkres)  

  draw(map)
  frame(wks)
  
end 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;;       EXECUTAR NO TERMMINAL: $ ncl
;;                              load "estacoes_rs.ncl"
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
