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

var InterleavedBufferModel = require('./InterleavedBuffer.js').InterleavedBufferModel;

class InterleavedBufferAttributeModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            data: null,
            itemSize: 0,
            offset: 0,
            normalized: false,

        });
    }

    constructThreeObject() {

        var result = new THREE.InterleavedBufferAttribute(
            this.convertThreeTypeModelToThree(this.get('data'), 'data'),
            this.get('itemSize'),
            this.get('offset'),
            this.convertBoolModelToThree(this.get('normalized'), 'normalized')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('data');


        this.property_converters['data'] = 'convertThreeType';
        this.property_converters['itemSize'] = null;
        this.property_converters['offset'] = null;
        this.property_converters['normalized'] = 'convertBool';


    }
}

InterleavedBufferAttributeModel.model_name = 'InterleavedBufferAttributeModel';
InterleavedBufferAttributeModel.serializers = {
    ...ThreeModel.serializers,
    data: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    InterleavedBufferAttributeModel: InterleavedBufferAttributeModel,
};
