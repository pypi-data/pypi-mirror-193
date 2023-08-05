//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;


class BufferAttributeModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            array: undefined,
            dynamic: false,
            needsUpdate: false,
            normalized: false,
            version: -1,

        });
    }

    constructThreeObject() {

        var result = new THREE.BufferAttribute(
            this.convertArrayBufferModelToThree(this.get('array'), 'array'),
            this.convertBoolModelToThree(this.get('normalized'), 'normalized')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.datawidget_properties.push('array');

        this.props_created_by_three['version'] = true;
        this.props_created_by_three['needsUpdate'] = true;

        this.property_converters['array'] = 'convertArrayBuffer';
        this.property_converters['dynamic'] = 'convertBool';
        this.property_converters['needsUpdate'] = 'convertBool';
        this.property_converters['normalized'] = 'convertBool';
        this.property_converters['version'] = null;


    }
}

BufferAttributeModel.model_name = 'BufferAttributeModel';
BufferAttributeModel.serializers = {
    ...ThreeModel.serializers,
    array: dataserializers.data_union_serialization,
};

module.exports = {
    BufferAttributeModel: BufferAttributeModel,
};
