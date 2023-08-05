//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;

var CurveModel = require('../extras/core/Curve.autogen.js').CurveModel;

class TubeGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            path: null,
            segments: 64,
            radius: 1,
            radialSegments: 8,
            close: false,
            type: "TubeGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.TubeGeometry(
            this.convertThreeTypeModelToThree(this.get('path'), 'path'),
            this.get('segments'),
            this.convertFloatModelToThree(this.get('radius'), 'radius'),
            this.get('radialSegments'),
            this.convertBoolModelToThree(this.get('close'), 'close')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('path');

        this.props_created_by_three['type'] = true;

        this.property_converters['path'] = 'convertThreeType';
        this.property_converters['segments'] = null;
        this.property_converters['radius'] = 'convertFloat';
        this.property_converters['radialSegments'] = null;
        this.property_converters['close'] = 'convertBool';
        this.property_converters['type'] = null;


    }
}

TubeGeometryModel.model_name = 'TubeGeometryModel';
TubeGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
    path: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    TubeGeometryModel: TubeGeometryModel,
};
