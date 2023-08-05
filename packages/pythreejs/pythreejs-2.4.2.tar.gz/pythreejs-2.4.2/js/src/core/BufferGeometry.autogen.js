//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseBufferGeometryModel = require('./BaseBufferGeometry.autogen.js').BaseBufferGeometryModel;

var BufferAttributeModel = require('./BufferAttribute.js').BufferAttributeModel;
var InterleavedBufferAttributeModel = require('./InterleavedBufferAttribute.autogen.js').InterleavedBufferAttributeModel;
var BaseGeometryModel = require('./BaseGeometry.autogen.js').BaseGeometryModel;

class BufferGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            index: null,
            attributes: {},
            morphAttributes: {},
            userData: {},
            MaxIndex: 65535,
            _ref_geometry: null,
            _store_ref: false,
            type: "BufferGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.BufferGeometry();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('index');
        this.three_nested_properties.push('attributes');
        this.three_nested_properties.push('morphAttributes');
        this.three_properties.push('_ref_geometry');

        this.props_created_by_three['type'] = true;

        this.property_converters['index'] = 'convertThreeType';
        this.property_converters['attributes'] = 'convertThreeTypeDict';
        this.property_converters['morphAttributes'] = 'convertMorphAttributes';
        this.property_converters['userData'] = null;
        this.property_converters['MaxIndex'] = null;
        this.property_converters['_ref_geometry'] = 'convertThreeType';
        this.property_converters['_store_ref'] = 'convertBool';
        this.property_converters['type'] = null;

        this.property_assigners['userData'] = 'assignDict';

    }
}

BufferGeometryModel.model_name = 'BufferGeometryModel';
BufferGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
    index: { deserialize: serializers.unpackThreeModel },
    attributes: { deserialize: serializers.unpackThreeModel },
    morphAttributes: { deserialize: serializers.unpackThreeModel },
    _ref_geometry: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    BufferGeometryModel: BufferGeometryModel,
};
