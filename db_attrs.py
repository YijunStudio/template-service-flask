FULLCOLS = {
    'view_area': ['id', 'type', 'name',
                  'length', 'width', 'height',
                  'xAxis', 'yAxis', 'zAxis', 'degree',
                  'xAxisCenter', 'yAxisCenter', 'zAxisCenter',
                  'comment', 'warehouse_id', 'material_count'],
    'view_equipment': ['id', 'type',
                       'model_id', 'model_name', 'model_properties',
                       'status', 'purchaseTime', 'startTime', 'lastModifiedTime', 'expiredTime',
                       'comment', 'maxHeight', 'warehouse_id'],
    'view_equipmentmodel': ['id', 'name', 'type', 'properties'],
    'view_material': ['id', 'areaSeq', 'createTime', 'removeTime',
                      'model_id', 'model_name', 'model_raws', 'model_thickness', 'model_length', 'model_width', 'model_height',
                      'model_xAxisDelta', 'model_yAxisDelta', 'model_zAxisDelta',
                      'area_id', 'area_type', 'area_name', 'area_length', 'area_width', 'area_height',
                      'area_xAxis', 'area_yAxis', 'area_zAxis', 'area_degree', 'area_xAxisCenter', 'area_yAxisCenter', 'area_zAxisCenter', 'area_comment',
                      'warehouse_id', 'warehouse_name', 'warehouse_address', 'warehouse_length', 'warehouse_width', 'warehouse_height', 'warehouse_maxHeight', 'warehouse_comment'],
    'view_materialmodel': ['id', 'name', 'raws', 'thickness', 'length', 'width', 'height', 'xAxisDelta', 'yAxisDelta', 'zAxisDelta'],
    'view_task': ['id',
                  'crane_id', 'model_type', 'model_id', 'model_name', 'model_properties', 'model_status',
                  'status',
                  'sourceArea_id', 'sourceArea_type', 'sourceArea_name', 'sourceArea_length', 'sourceArea_width', 'sourceArea_height',
                  'sourceArea_xAxis', 'sourceArea_yAxis', 'sourceArea_zAxis', 'sourceArea_degree',
                  'sourceArea_xAxisCenter', 'sourceArea_yAxisCenter', 'sourceArea_zAxisCenter', 'sourceArea_comment',
                  'targetArea_id', 'targetArea_type', 'targetArea_name', 'targetArea_length', 'targetArea_width', 'targetArea_height',
                  'targetArea_xAxis', 'targetArea_yAxis', 'targetArea_zAxis', 'targetArea_degree',
                  'targetArea_xAxisCenter', 'targetArea_yAxisCenter', 'targetArea_zAxisCenter', 'targetArea_comment',
                  'materials', 'actionSeq',
                  'sendTime', 'startTime', 'endTime', 'warehouse_id'],
    'view_warehouse': ['id', 'name', 'address', 'length',
                       'width', 'height', 'maxHeight', 'comment'],
    'view_user': ['id', 'username', 'password', 'is_full_authority', 'authorities', 'phone', 'email', 'is_active'],
}