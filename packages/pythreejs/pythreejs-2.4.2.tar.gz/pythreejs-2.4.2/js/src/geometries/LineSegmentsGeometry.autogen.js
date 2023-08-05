//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseBufferGeometryModel = require('../core/BaseBufferGeometry.autogen.js').BaseBufferGeometryModel;


class LineSegmentsGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            positions: undefined,
            colors: null,
            type: "LineSegmentsGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.LineSegmentsGeometry();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);
        this.datawidget_properties.push('positions');
        this.datawidget_properties.push('colors');

        this.props_created_by_three['type'] = true;

        this.property_converters['positions'] = 'convertArrayBuffer';
        this.property_converters['colors'] = 'convertArrayBuffer';
        this.property_converters['type'] = null;


    }
}

LineSegmentsGeometryModel.model_name = 'LineSegmentsGeometryModel';
LineSegmentsGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
    positions: dataserializers.data_union_serialization,
    colors: dataserializers.data_union_serialization,
};

module.exports = {
    LineSegmentsGeometryModel: LineSegmentsGeometryModel,
};
