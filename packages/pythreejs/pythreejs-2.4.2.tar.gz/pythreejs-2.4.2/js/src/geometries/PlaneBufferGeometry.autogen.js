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


class PlaneBufferGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            width: 1,
            height: 1,
            widthSegments: 1,
            heightSegments: 1,
            type: "PlaneBufferGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.PlaneBufferGeometry(
            this.convertFloatModelToThree(this.get('width'), 'width'),
            this.convertFloatModelToThree(this.get('height'), 'height'),
            this.get('widthSegments'),
            this.get('heightSegments')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['width'] = 'convertFloat';
        this.property_converters['height'] = 'convertFloat';
        this.property_converters['widthSegments'] = null;
        this.property_converters['heightSegments'] = null;
        this.property_converters['type'] = null;


    }
}

PlaneBufferGeometryModel.model_name = 'PlaneBufferGeometryModel';
PlaneBufferGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
};

module.exports = {
    PlaneBufferGeometryModel: PlaneBufferGeometryModel,
};
