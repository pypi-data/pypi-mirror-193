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

var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;

class EdgesGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            geometry: null,
            thresholdAngle: 1,
            type: "EdgesGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.EdgesGeometry(
            this.convertThreeTypeModelToThree(this.get('geometry'), 'geometry'),
            this.convertFloatModelToThree(this.get('thresholdAngle'), 'thresholdAngle')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('geometry');

        this.props_created_by_three['type'] = true;

        this.property_converters['geometry'] = 'convertThreeType';
        this.property_converters['thresholdAngle'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

EdgesGeometryModel.model_name = 'EdgesGeometryModel';
EdgesGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
    geometry: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    EdgesGeometryModel: EdgesGeometryModel,
};
