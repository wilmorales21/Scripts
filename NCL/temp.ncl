load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"

begin

 arq = asciiread("dados.txt",-1,"string")

 temp = stringtofloat(str_get_field(arq,3," "))
 lat = stringtofloat(str_get_field(arq,1," ")) 
 lon = stringtofloat(str_get_field(arq,2," "))

;Este comando vai deslocar o texto(informações de temperatura) em 0.10 graus de latitude para cima(+) do marcador no mapa.
 lat2 = lat + 0.10     

; printVarSummary(temp)
 temp@_FillValue = -999.9   

 wks = gsn_open_wks("png","temperaturas")
 gsn_define_colormap(wks,"MPL_rainbow")

 res                             = True
 res@gsnMaximize                 = True
 res@gsnFrame                    = False   ; não avança o quadro.
 res@gsnAddCyclic                = False

 res@cnLevelSelectionMode        = "ManualLevels"
 res@cnMinLevelValF              = 7        ;Valor mínimo na barra de cores 	 
 res@cnMaxLevelValF              = 19		;Valor máximo na barra de cores
 res@cnLevelSpacingF             = 0.50     ;Espaçamento entre as cores

 res@lbOrientation               = "vertical"   ;Orientação da barra de cores
 res@lbBoxLinesOn                = False        ;Desabilita linhas entre as cores  

 res@sfXArray                    = lon
 res@sfYArray                    = lat

;Zoom no mapa sobre a área de interesse
  res@mpMinLatF                  = min(lat)-.5
  res@mpMinLonF                  = min(lon)-.5
  res@mpMaxLatF                  = max(lat)+.5
  res@mpMaxLonF                  = max(lon)+.5

  res@cnFillOn                   = True   ; Habilita gráfico preenchido
  res@cnLinesOn                  = False  ; Desabilita as isolinhas 
  res@cnSmoothingOn              = True   ;
  res@cnSmoothingTensionF        = 2
  res@cnSmoothingDistanceF       = 0.005
  res@mpLandFillColor            ="white" ; Mapa com fundo branco
 
  res@pmTickMarkDisplayMode      = "Always"
  res@mpDataSetName              = "Earth..4"
  res@mpOutlineOn                = True
  res@mpDataBaseVersion          = "MediumRes" 
  res@mpOutlineBoundarySets      = "AllBoundaries"
  res@mpOutlineSpecifiers        = (/"Brazil:states"/)
  res@mpFillAreaSpecifiers       = (/"Land", "Brazil:Rio Grande do Sul"/)
  res@mpSpecifiedFillColors      = (/0,-1,0/)

;-------------------------------------------------------------------------------
; Códigos do cedilha, til, acento agudo, acento circunflexo e acento grave no NCL

  cedil = "c~H-13F35~K~FH2~"
  otilde = "o~H-13V2F35~D~FV-2H3~" 
  aacute = "a~H-13V2F35~B~FV-2H3~"
  agrave = "a~H-13V2F35~A~FV-2H3~"
  acirc  = "a~H-13V2F35~C~FV-2H3~"

;Plota o titulo da figura
  res@gsnCenterString  =  "~Z80~Temperatura instant"+acirc+"nea nas esta"+cedil+otilde+"es autom"+aacute+"ticas ~C~              do INMET "+agrave+"s 06UTC de 03/04/2020"

  plot = gsn_csm_contour_map(wks,temp,res)

;Anexa marcadores ao mapa(plota o ponto de latitude e longitude das estações)
  mkres               = True
  mkres@gsMarkerIndex = 16     ;Círculo cheio
  mkres@gsMarkerSizeF = 8      ;Tamanho do círculo  
  markers = gsn_add_polymarker(wks,plot,lon,lat,mkres)

;Anexa texto ao mapa(plota as informações de temperatura)
  txres               = True
  txres@txFontHeightF = 0.014           ;Tamanho do texto   
  txres@txJust        = "BottomCenter"  ;Texto centralizado em cima do marcador 
  txres@txFontColor   = "black"         ;Cor das informações de texto
  texto = gsn_add_text(wks,plot,temp,lon,lat2,txres) 

  draw(plot)
  frame(wks)
end 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;;       EXECUTAR NO TERMMINAL: $ ncl
;;                              load "temp.ncl"
;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
